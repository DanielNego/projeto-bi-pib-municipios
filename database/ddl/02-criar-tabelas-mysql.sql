-- =====================================================================
-- Projeto BI: PIB dos Municipios Brasileiros (IBGE, 2010-2023)
-- Script para o MySQL Workbench (File > Import > Reverse Engineer MySQL Create Script)
-- Modelo multidimensional: 1 tabela fato + 4 dimensoes
-- Disciplina: Laboratorio de Inovacao IV - Prof. Edilberto Silva
-- Grupo: grupo03 - PIB Municipios
-- =====================================================================

CREATE SCHEMA IF NOT EXISTS pib_municipios DEFAULT CHARACTER SET utf8mb4;
USE pib_municipios;

-- Dimensao Regiao: as 5 grandes regioes do Brasil
CREATE TABLE dim_regiao (
    cod_regiao   SMALLINT     NOT NULL,
    nome_regiao  VARCHAR(20)  NOT NULL,
    PRIMARY KEY (cod_regiao)
) ENGINE = InnoDB;

-- Dimensao UF: os 27 estados (cada um pertence a uma regiao)
CREATE TABLE dim_uf (
    cod_uf      SMALLINT     NOT NULL,
    sigla_uf    CHAR(2)      NOT NULL,
    nome_uf     VARCHAR(30)  NOT NULL,
    cod_regiao  SMALLINT     NOT NULL,
    PRIMARY KEY (cod_uf),
    CONSTRAINT fk_uf_regiao FOREIGN KEY (cod_regiao) REFERENCES dim_regiao (cod_regiao)
) ENGINE = InnoDB;

-- Dimensao Municipio: os 5.570 municipios (cada um pertence a uma UF)
CREATE TABLE dim_municipio (
    cod_municipio   INT          NOT NULL,
    nome_municipio  VARCHAR(60)  NOT NULL,
    cod_uf          SMALLINT     NOT NULL,
    PRIMARY KEY (cod_municipio),
    CONSTRAINT fk_municipio_uf FOREIGN KEY (cod_uf) REFERENCES dim_uf (cod_uf)
) ENGINE = InnoDB;

-- Dimensao Tempo: os anos disponiveis na base (2010 a 2023)
CREATE TABLE dim_tempo (
    ano  SMALLINT  NOT NULL,
    PRIMARY KEY (ano)
) ENGINE = InnoDB;

-- Tabela Fato: PIB e PIB per capita de cada municipio em cada ano
CREATE TABLE fato_pib (
    cod_municipio   INT            NOT NULL,
    ano             SMALLINT       NOT NULL,
    pib             DECIMAL(18,3)  NOT NULL,
    pib_per_capita  DECIMAL(14,2)  NOT NULL,
    PRIMARY KEY (cod_municipio, ano),
    CONSTRAINT fk_fato_municipio FOREIGN KEY (cod_municipio) REFERENCES dim_municipio (cod_municipio),
    CONSTRAINT fk_fato_tempo FOREIGN KEY (ano) REFERENCES dim_tempo (ano)
) ENGINE = InnoDB;
