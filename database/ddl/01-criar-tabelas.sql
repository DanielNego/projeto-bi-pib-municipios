-- =====================================================================
-- Projeto BI: PIB dos Municipios Brasileiros (IBGE, 2010-2023)
-- Script DDL do modelo dimensional (esquema estrela)
-- Disciplina: Laboratorio de Inovacao IV - Prof. Edilberto Silva
-- Grupo: grupo03 - PIB Municipios
-- SQL padrao (funciona com poucos ajustes em SQL Server, PostgreSQL e MySQL)
-- =====================================================================

-- Dimensao Regiao: as 5 grandes regioes do Brasil
CREATE TABLE dim_regiao (
    cod_regiao   SMALLINT     NOT NULL,
    nome_regiao  VARCHAR(20)  NOT NULL,
    CONSTRAINT pk_dim_regiao PRIMARY KEY (cod_regiao)
);

-- Dimensao UF: os 27 estados (cada um pertence a uma regiao)
CREATE TABLE dim_uf (
    cod_uf      SMALLINT     NOT NULL,
    sigla_uf    CHAR(2)      NOT NULL,
    nome_uf     VARCHAR(30)  NOT NULL,
    cod_regiao  SMALLINT     NOT NULL,
    CONSTRAINT pk_dim_uf PRIMARY KEY (cod_uf),
    CONSTRAINT fk_uf_regiao FOREIGN KEY (cod_regiao) REFERENCES dim_regiao (cod_regiao)
);

-- Dimensao Municipio: os 5.570 municipios (cada um pertence a uma UF)
-- O nome NAO e unico (ha municipios com o mesmo nome em UFs diferentes),
-- por isso a chave primaria e o codigo do IBGE.
CREATE TABLE dim_municipio (
    cod_municipio   INT          NOT NULL,
    nome_municipio  VARCHAR(60)  NOT NULL,
    cod_uf          SMALLINT     NOT NULL,
    CONSTRAINT pk_dim_municipio PRIMARY KEY (cod_municipio),
    CONSTRAINT fk_municipio_uf FOREIGN KEY (cod_uf) REFERENCES dim_uf (cod_uf)
);

-- Dimensao Tempo: os anos disponiveis na base (2010 a 2023)
CREATE TABLE dim_tempo (
    ano  SMALLINT  NOT NULL,
    CONSTRAINT pk_dim_tempo PRIMARY KEY (ano)
);

-- Tabela Fato: PIB e PIB per capita de cada municipio em cada ano
-- Obs.: nao ha CHECK (pib >= 0) de proposito, pois a base do IBGE tem
-- 1 registro com PIB negativo (Guamare/RN, 2012).
CREATE TABLE fato_pib (
    cod_municipio   INT            NOT NULL,
    ano             SMALLINT       NOT NULL,
    pib             DECIMAL(18,3)  NOT NULL,  -- R$ 1.000, a precos correntes
    pib_per_capita  DECIMAL(14,2)  NOT NULL,  -- R$ 1,00, a precos correntes
    CONSTRAINT pk_fato_pib PRIMARY KEY (cod_municipio, ano),
    CONSTRAINT fk_fato_municipio FOREIGN KEY (cod_municipio) REFERENCES dim_municipio (cod_municipio),
    CONSTRAINT fk_fato_tempo FOREIGN KEY (ano) REFERENCES dim_tempo (ano)
);
