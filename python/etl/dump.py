"""Etapa 4 - Dumps dos bancos (staging e MMD) com o mysqldump."""
import glob
import os
import shutil
import subprocess

import config


def achar_mysqldump():
    exe = shutil.which("mysqldump")
    if exe:
        return exe
    for padrao in (
        "C:/Program Files/MySQL/MySQL Server */bin/mysqldump.exe",
        "C:/Program Files (x86)/MySQL/MySQL Server */bin/mysqldump.exe",
    ):
        achados = sorted(glob.glob(padrao))
        if achados:
            return achados[-1]
    return None


def montar_comando(exe, banco, destino):
    return [
        exe,
        f"--host={config.MYSQL_HOST}",
        f"--port={config.MYSQL_PORT}",
        f"--user={config.MYSQL_USER}",
        "--default-character-set=utf8mb4",
        "--databases", banco,
        f"--result-file={destino}",
    ]


def gerar_dumps():
    exe = achar_mysqldump()
    if exe is None:
        print("[dump] mysqldump nao encontrado. Gere os dumps pelo MySQL Workbench:")
        print("       Server > Data Export > marque staging_pib e pib_municipios >")
        print("       'Export to Self-Contained File' (um arquivo por banco) em database/dumps/")
        return False

    config.PASTA_DUMPS.mkdir(parents=True, exist_ok=True)
    ambiente = dict(os.environ, MYSQL_PWD=config.obter_senha())  # evita a senha na linha de comando
    for banco, arquivo in ((config.BD_STAGING, "dump-staging.sql"), (config.BD_MMD, "dump-mmd.sql")):
        destino = config.PASTA_DUMPS / arquivo
        subprocess.run(montar_comando(exe, banco, destino), check=True, env=ambiente)
        print(f"[dump] {banco} -> {destino}")
    return True
