"""Orquestracao do ETL do projeto PIB dos Municipios.

Uso (a partir da raiz do repositorio):
    python python/etl/main.py                 # roda tudo
    python python/etl/main.py --etapa tratar  # roda so uma etapa

Etapas: extrair, tratar, staging, mmd, dump  (ou "tudo")
"""
import argparse

import dump
import extract
import load
import transform


def main():
    parser = argparse.ArgumentParser(description="ETL do PIB dos Municipios (IBGE)")
    parser.add_argument("--etapa", default="tudo", choices=["tudo", "extrair", "tratar", "staging", "mmd", "dump"])
    etapa = parser.parse_args().etapa

    if etapa in ("tudo", "extrair"):
        extract.extrair()
    if etapa in ("tudo", "tratar"):
        transform.tratar()
    if etapa in ("tudo", "staging", "mmd"):
        conn = load.conectar()
        try:
            if etapa in ("tudo", "staging"):
                load.carregar_staging(conn)
            if etapa in ("tudo", "mmd"):
                load.carregar_mmd(conn)
        finally:
            conn.close()
    if etapa in ("tudo", "dump"):
        dump.gerar_dumps()


if __name__ == "__main__":
    main()
