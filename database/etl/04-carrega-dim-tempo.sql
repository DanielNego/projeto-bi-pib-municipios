-- Carga da dimensao Tempo (anos de 2010 a 2023) a partir do staging
INSERT INTO pib_municipios.dim_tempo (ano)
SELECT DISTINCT ano
FROM staging_pib.stg_pib_municipios
ORDER BY ano;
