-- Carga da dimensao UF (27 estados) a partir do staging
INSERT INTO pib_municipios.dim_uf (cod_uf, sigla_uf, nome_uf, cod_regiao)
SELECT DISTINCT cod_uf, sigla_uf, nome_uf, cod_regiao
FROM staging_pib.stg_pib_municipios
ORDER BY cod_uf;
