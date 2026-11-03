-- =====================================================================
-- Conferencia da carga da tabela FATO (fato_pib)
-- =====================================================================

-- 1) Por ano: quantidade de registros e PIB somado no staging x na fato
SELECT s.ano,
       s.registros_staging,
       f.registros_fato,
       s.pib_staging,
       f.pib_fato,
       CASE WHEN s.registros_staging = f.registros_fato AND s.pib_staging = f.pib_fato
            THEN 'OK' ELSE 'DIVERGENTE' END AS situacao
FROM (SELECT ano, COUNT(*) AS registros_staging, ROUND(SUM(pib), 3) AS pib_staging
      FROM staging_pib.stg_pib_municipios GROUP BY ano) s
JOIN (SELECT ano, COUNT(*) AS registros_fato, ROUND(SUM(pib), 3) AS pib_fato
      FROM pib_municipios.fato_pib GROUP BY ano) f ON f.ano = s.ano
ORDER BY s.ano;

-- 2) Registros com PIB ou PIB per capita menor ou igual a zero (problema PQ-03 da Fase 2)
SELECT m.nome_municipio, u.sigla_uf, f.ano, f.pib, f.pib_per_capita
FROM pib_municipios.fato_pib f
JOIN pib_municipios.dim_municipio m ON m.cod_municipio = f.cod_municipio
JOIN pib_municipios.dim_uf u ON u.cod_uf = m.cod_uf
WHERE f.pib <= 0 OR f.pib_per_capita <= 0;

-- 3) Teste do esquema estrela: os 5 maiores PIB de 2023, juntando a fato com todas as dimensoes
SELECT m.nome_municipio, u.sigla_uf, r.nome_regiao, f.pib
FROM pib_municipios.fato_pib f
JOIN pib_municipios.dim_tempo t ON t.ano = f.ano
JOIN pib_municipios.dim_municipio m ON m.cod_municipio = f.cod_municipio
JOIN pib_municipios.dim_uf u ON u.cod_uf = m.cod_uf
JOIN pib_municipios.dim_regiao r ON r.cod_regiao = u.cod_regiao
WHERE t.ano = 2023
ORDER BY f.pib DESC
LIMIT 5;
