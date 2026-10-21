-- Apaga o banco do modelo multidimensional (MMD) para a carga poder ser
-- repetida do zero. Depois, o script database/ddl/02-criar-tabelas-mysql.sql
-- recria o schema e as tabelas.
DROP DATABASE IF EXISTS pib_municipios;
