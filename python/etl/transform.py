"""Etapa 2 - Tratamento.

Aplica o plano de tratamento da Fase 2 (02-data-understanding.md) no CSV da fonte
e gera o CSV tratado, que e o que vai para o staging.
"""
import pandas as pd

import config

CAMPOS_TEXTO = ["nome_regiao", "sigla_uf", "nome_uf", "nome_municipio"]
CAMPOS_INTEIROS = ["ano", "cod_regiao", "cod_uf", "cod_municipio"]

# O IBGE grafa "Centro-oeste"; o nome oficial da regiao e "Centro-Oeste"
PADRAO_REGIAO = {"Centro-oeste": "Centro-Oeste"}


def tratar():
    df = pd.read_csv(config.CSV_FONTE, sep=";", encoding="utf-8-sig")
    relatorio = [f"Registros lidos do CSV da fonte: {len(df)}"]

    # 1) Tirar espacos sobrando dos textos
    for campo in CAMPOS_TEXTO:
        df[campo] = df[campo].str.strip()

    # 2) Padronizar o nome da regiao
    alterados = int(df["nome_regiao"].isin(PADRAO_REGIAO).sum())
    df["nome_regiao"] = df["nome_regiao"].replace(PADRAO_REGIAO)
    relatorio.append(f"Nome de regiao padronizado (Centro-oeste -> Centro-Oeste): {alterados} registros")

    # 3) Nenhum campo pode estar nulo (o staging e a fato exigem todos)
    nulos = df.isnull().sum()
    if nulos.sum() > 0:
        raise ValueError(f"Existem valores nulos nos campos usados:\n{nulos[nulos > 0]}")
    relatorio.append("Valores nulos nos campos usados: 0")

    # 4) Duplicados na chave (municipio + ano)
    duplicados = int(df.duplicated(subset=["ano", "cod_municipio"]).sum())
    df = df.drop_duplicates(subset=["ano", "cod_municipio"])
    relatorio.append(f"Registros duplicados (municipio + ano) removidos: {duplicados}")

    # 5) Cada codigo deve ter sempre o mesmo nome e a mesma UF (senao as dimensoes quebram)
    if df.groupby("cod_municipio")[["nome_municipio", "cod_uf"]].nunique().max().max() > 1:
        raise ValueError("Ha municipio com mais de um nome ou mais de uma UF.")
    if df.groupby("cod_uf")[["sigla_uf", "nome_uf", "cod_regiao"]].nunique().max().max() > 1:
        raise ValueError("Ha UF com mais de um nome ou mais de uma regiao.")
    relatorio.append("Codigos consistentes: cada municipio tem 1 nome e 1 UF; cada UF tem 1 regiao")

    # 6) Tipos dos dados
    df[CAMPOS_INTEIROS] = df[CAMPOS_INTEIROS].astype(int)
    df["pib"] = df["pib"].astype(float)
    df["pib_per_capita"] = df["pib_per_capita"].astype(float)

    # 7) Avisos (problemas PQ-02 e PQ-03 do documento da Fase 2): os registros sao MANTIDOS
    total_anos = df["ano"].nunique()
    anos_por_municipio = df.groupby(["cod_municipio", "nome_municipio", "sigla_uf"])["ano"].nunique()
    incompletos = anos_por_municipio[anos_por_municipio < total_anos]
    relatorio.append(f"PQ-02 - municipios que nao aparecem em todos os {total_anos} anos (mantidos): {len(incompletos)}")
    for (cod, nome, uf), qtd in incompletos.items():
        primeiro = int(df[df["cod_municipio"] == cod]["ano"].min())
        relatorio.append(f"   - {nome} ({uf}): {qtd} anos, a partir de {primeiro}")

    negativos = df[(df["pib"] <= 0) | (df["pib_per_capita"] <= 0)]
    relatorio.append(f"PQ-03 - registros com PIB ou PIB per capita menor ou igual a zero (mantidos): {len(negativos)}")
    for _, linha in negativos.iterrows():
        relatorio.append(f"   - {linha['nome_municipio']} ({linha['sigla_uf']}), {linha['ano']}: PIB = {linha['pib']}")

    relatorio.append(f"Registros no CSV tratado: {len(df)}")

    df.to_csv(config.CSV_TRATADO, sep=";", index=False, encoding="utf-8-sig")
    config.RELATORIO_TRATAMENTO.write_text("\n".join(relatorio) + "\n", encoding="utf-8")
    print("[tratar]\n  " + "\n  ".join(relatorio))
    return df


if __name__ == "__main__":
    tratar()
