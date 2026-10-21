-- Conferencia da carga: quantidade de registros em cada tabela
SELECT 'staging_pib.stg_pib_municipios' AS tabela, COUNT(*) AS registros FROM staging_pib.stg_pib_municipios
UNION ALL SELECT 'pib_municipios.dim_regiao', COUNT(*) FROM pib_municipios.dim_regiao
UNION ALL SELECT 'pib_municipios.dim_uf', COUNT(*) FROM pib_municipios.dim_uf
UNION ALL SELECT 'pib_municipios.dim_municipio', COUNT(*) FROM pib_municipios.dim_municipio
UNION ALL SELECT 'pib_municipios.dim_tempo', COUNT(*) FROM pib_municipios.dim_tempo
UNION ALL SELECT 'pib_municipios.fato_pib', COUNT(*) FROM pib_municipios.fato_pib;

-- Conferencia: o PIB somado tem que ser igual no staging e na fato
SELECT 'PIB somado no staging (R$ mil)' AS conferencia, ROUND(SUM(pib), 3) AS valor FROM staging_pib.stg_pib_municipios
UNION ALL SELECT 'PIB somado na fato (R$ mil)', ROUND(SUM(pib), 3) FROM pib_municipios.fato_pib;

-- Conferencia: registros orfaos (todos devem dar 0)
SELECT 'fato sem municipio' AS conferencia, COUNT(*) AS orfaos
FROM pib_municipios.fato_pib f
LEFT JOIN pib_municipios.dim_municipio m ON m.cod_municipio = f.cod_municipio
WHERE m.cod_municipio IS NULL
UNION ALL
SELECT 'fato sem ano', COUNT(*)
FROM pib_municipios.fato_pib f
LEFT JOIN pib_municipios.dim_tempo t ON t.ano = f.ano
WHERE t.ano IS NULL
UNION ALL
SELECT 'municipio sem UF', COUNT(*)
FROM pib_municipios.dim_municipio m
LEFT JOIN pib_municipios.dim_uf u ON u.cod_uf = m.cod_uf
WHERE u.cod_uf IS NULL
UNION ALL
SELECT 'UF sem regiao', COUNT(*)
FROM pib_municipios.dim_uf u
LEFT JOIN pib_municipios.dim_regiao r ON r.cod_regiao = u.cod_regiao
WHERE r.cod_regiao IS NULL;
