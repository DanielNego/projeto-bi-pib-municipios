-- =====================================================================
-- Projeto BI: PIB dos Municipios Brasileiros (IBGE, 2010-2023)
-- Banco de STAGING: area de passagem, com os dados do CSV exatamente
-- como chegaram (ja tratados pelo script transform.py).
-- Disciplina: Laboratorio de Inovacao IV - Prof. Edilberto Silva
-- Grupo: grupo03 - PIB Municipios
-- =====================================================================

DROP DATABASE IF EXISTS staging_pib;
CREATE DATABASE staging_pib DEFAULT CHARACTER SET utf8mb4;
USE staging_pib;

-- Uma linha por municipio por ano (mesma granularidade da fonte do IBGE).
-- Staging nao tem chaves nem relacionamentos: so guarda os dados da carga.
CREATE TABLE stg_pib_municipios (
    ano             SMALLINT       NOT NULL,
    cod_regiao      SMALLINT       NOT NULL,
    nome_regiao     VARCHAR(30)    NOT NULL,
    cod_uf          SMALLINT       NOT NULL,
    sigla_uf        CHAR(2)        NOT NULL,
    nome_uf         VARCHAR(40)    NOT NULL,
    cod_municipio   INT            NOT NULL,
    nome_municipio  VARCHAR(80)    NOT NULL,
    pib             DECIMAL(18,3)  NOT NULL,
    pib_per_capita  DECIMAL(14,2)  NOT NULL,
    dt_carga        DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB;
