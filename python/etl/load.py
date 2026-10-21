"""Etapa 3 - Carga.

- carregar_staging: cria o banco de staging e carrega o CSV tratado nele.
- carregar_mmd: recria o modelo multidimensional (MMD) e carrega as dimensoes
  e a fato a partir do staging, usando os scripts SQL de database/etl/.
"""
import pandas as pd

import config

COLUNAS_STAGING = [
    "ano", "cod_regiao", "nome_regiao", "cod_uf", "sigla_uf", "nome_uf",
    "cod_municipio", "nome_municipio", "pib", "pib_per_capita",
]
TAMANHO_LOTE = 5000


def conectar():
    import mysql.connector  # instalado com: pip install mysql-connector-python

    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        port=config.MYSQL_PORT,
        user=config.MYSQL_USER,
        password=config.obter_senha(),
        charset="utf8mb4",
    )


def ler_comandos(caminho):
    """Le um arquivo .sql e devolve a lista de comandos (separados por ;)."""
    linhas = [l for l in caminho.read_text(encoding="utf-8").splitlines() if not l.strip().startswith("--")]
    return [c.strip() for c in "\n".join(linhas).split(";") if c.strip()]


def executar_arquivo_sql(cursor, caminho, mostrar_resultados=False):
    print(f"[sql] {caminho.name}")
    for comando in ler_comandos(caminho):
        cursor.execute(comando)
        if mostrar_resultados and comando.upper().startswith("SELECT"):
            for linha in cursor.fetchall():
                print("      ", *linha)


def carregar_staging(conn, df=None):
    if df is None:
        df = pd.read_csv(config.CSV_TRATADO, sep=";", encoding="utf-8-sig")
    cursor = conn.cursor()
    executar_arquivo_sql(cursor, config.PASTA_SQL_DDL / "03-criar-staging.sql")

    colunas = ", ".join(COLUNAS_STAGING)
    parametros = ", ".join(["%s"] * len(COLUNAS_STAGING))
    insert = f"INSERT INTO {config.BD_STAGING}.stg_pib_municipios ({colunas}) VALUES ({parametros})"

    # astype(object) transforma os numeros do pandas em int/float normais do Python
    linhas = list(df[COLUNAS_STAGING].astype(object).itertuples(index=False, name=None))
    for inicio in range(0, len(linhas), TAMANHO_LOTE):
        cursor.executemany(insert, linhas[inicio:inicio + TAMANHO_LOTE])
    conn.commit()
    print(f"[staging] {len(linhas)} registros carregados em {config.BD_STAGING}.stg_pib_municipios")


def carregar_mmd(conn):
    cursor = conn.cursor()
    executar_arquivo_sql(cursor, config.PASTA_SQL_ETL / "00-limpar-mmd.sql")
    executar_arquivo_sql(cursor, config.PASTA_SQL_DDL / "02-criar-tabelas-mysql.sql")
    for arquivo in sorted(config.PASTA_SQL_ETL.glob("0[1-5]-*.sql")):
        executar_arquivo_sql(cursor, arquivo)
    conn.commit()
    print("[mmd] dimensoes e fato carregadas. Conferencia da carga:")
    executar_arquivo_sql(cursor, config.PASTA_SQL_ETL / "06-validacao-carga.sql", mostrar_resultados=True)
