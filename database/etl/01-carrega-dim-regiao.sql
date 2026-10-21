-- Carga da dimensao Regiao (5 regioes) a partir do staging
INSERT INTO pib_municipios.dim_regiao (cod_regiao, nome_regiao)
SELECT DISTINCT cod_regiao, nome_regiao
FROM staging_pib.stg_pib_municipios
ORDER BY cod_regiao;
