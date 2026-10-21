"""Configuracoes do projeto (caminhos, nomes dos bancos e conexao com o MySQL)."""
import getpass
import os
from pathlib import Path

# Raiz do repositorio (este arquivo fica em python/etl/)
RAIZ = Path(__file__).resolve().parents[2]

# Arquivos de dados
ARQUIVO_XLSX = RAIZ / "dados" / "PIB dos Municípios - base de dados 2010-2023.xlsx"
ABA_PIB = "PIB dos Municípios"
CSV_FONTE = RAIZ / "dados" / "csv" / "pib_municipios_fonte.csv"
CSV_TRATADO = RAIZ / "dados" / "csv" / "pib_municipios_tratado.csv"
RELATORIO_TRATAMENTO = RAIZ / "dados" / "csv" / "relatorio_tratamento.txt"

# Scripts SQL e dumps
PASTA_SQL_DDL = RAIZ / "database" / "ddl"
PASTA_SQL_ETL = RAIZ / "database" / "etl"
PASTA_DUMPS = RAIZ / "database" / "dumps"

# Bancos de dados no MySQL
BD_STAGING = "staging_pib"
BD_MMD = "pib_municipios"

# Conexao com o MySQL (pode ser trocada com variaveis de ambiente)
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", "3306"))
MYSQL_USER = os.environ.get("MYSQL_USER", "root")

_senha = os.environ.get("MYSQL_PASSWORD")


def obter_senha():
    """Usa a senha da variavel MYSQL_PASSWORD ou pergunta uma vez no terminal."""
    global _senha
    if _senha is None:
        _senha = getpass.getpass(f"Senha do MySQL (usuario {MYSQL_USER}): ")
    return _senha
