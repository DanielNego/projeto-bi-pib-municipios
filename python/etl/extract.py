"""Etapa 1 - Importacao.

Le a planilha do IBGE (xlsx) e gera o CSV da fonte de dados, so com os campos
usados no projeto e com nomes de colunas simples (a planilha original tem
quebras de linha dentro dos nomes das colunas).
"""
import pandas as pd

import config

# nome na planilha do IBGE -> nome no CSV / staging
COLUNAS = {
    "Ano": "ano",
    "Código da Grande Região": "cod_regiao",
    "Nome da Grande Região": "nome_regiao",
    "Código da Unidade da Federação": "cod_uf",
    "Sigla da Unidade da Federação": "sigla_uf",
    "Nome da Unidade da Federação": "nome_uf",
    "Código do Município": "cod_municipio",
    "Nome do Município": "nome_municipio",
}


def extrair():
    print(f"[extrair] Lendo a planilha: {config.ARQUIVO_XLSX.name}")
    dados = pd.read_excel(config.ARQUIVO_XLSX, sheet_name=config.ABA_PIB)

    # As colunas de PIB têm quebra de linha no nome, então procuramos pelo começo do texto
    col_pib = next(c for c in dados.columns if c.startswith("Produto Interno Bruto,"))
    col_pib_pc = next(c for c in dados.columns if "per capita" in c)

    mapa = {**COLUNAS, col_pib: "pib", col_pib_pc: "pib_per_capita"}
    fonte = dados[list(mapa)].rename(columns=mapa)

    config.CSV_FONTE.parent.mkdir(parents=True, exist_ok=True)
    fonte.to_csv(config.CSV_FONTE, sep=";", index=False, encoding="utf-8-sig")
    print(f"[extrair] {len(fonte)} registros salvos em {config.CSV_FONTE.name}")
    return fonte


if __name__ == "__main__":
    extrair()
