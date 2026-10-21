-- Carga da dimensao Municipio (5.570 municipios) a partir do staging
INSERT INTO pib_municipios.dim_municipio (cod_municipio, nome_municipio, cod_uf)
SELECT DISTINCT cod_municipio, nome_municipio, cod_uf
FROM staging_pib.stg_pib_municipios
ORDER BY cod_municipio;
