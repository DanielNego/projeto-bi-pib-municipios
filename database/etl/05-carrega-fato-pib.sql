-- Carga da tabela fato (PIB e PIB per capita por municipio e ano)
-- Precisa rodar depois das 4 dimensoes, por causa das chaves estrangeiras.
INSERT INTO pib_municipios.fato_pib (cod_municipio, ano, pib, pib_per_capita)
SELECT cod_municipio, ano, pib, pib_per_capita
FROM staging_pib.stg_pib_municipios
ORDER BY cod_municipio, ano;
