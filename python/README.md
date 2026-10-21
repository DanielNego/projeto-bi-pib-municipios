# ETL do projeto PIB dos Municípios

Scripts Python que importam, tratam e carregam os dados do IBGE no MySQL (staging e MMD).

## O que cada script faz

| Script | Etapa | O que faz |
| :---- | :---- | :---- |
| `etl/extract.py` | Importação | Lê a planilha do IBGE (`dados/*.xlsx`) e gera o CSV da fonte (`dados/csv/pib_municipios_fonte.csv`) |
| `etl/transform.py` | Tratamento | Aplica o plano de tratamento da Fase 2 e gera `pib_municipios_tratado.csv` e `relatorio_tratamento.txt` |
| `etl/load.py` | Carga | Carrega o CSV tratado no banco de staging e depois roda os SQLs de `database/etl/` para carregar o MMD |
| `etl/dump.py` | Dumps | Gera `database/dumps/dump-staging.sql` e `dump-mmd.sql` com o `mysqldump` |
| `etl/main.py` | Orquestração | Roda as etapas em ordem |
| `etl/config.py` | Configuração | Caminhos, nomes dos bancos e conexão com o MySQL |

## Fluxo dos dados

```
dados/*.xlsx (IBGE)
   │  extract.py
   ▼
dados/csv/pib_municipios_fonte.csv
   │  transform.py
   ▼
dados/csv/pib_municipios_tratado.csv
   │  load.py (carregar_staging)
   ▼
MySQL: staging_pib.stg_pib_municipios
   │  database/etl/01 a 05 (SQL)
   ▼
MySQL: pib_municipios (MMD): dim_regiao, dim_uf, dim_municipio, dim_tempo e fato_pib
```

## Como rodar

1. Ter o MySQL Server instalado e ligado, e o Python 3 instalado.
2. Na raiz do repositório, instalar as bibliotecas: `pip install -r python/requirements.txt`
3. Rodar tudo: `python python/etl/main.py`
   - O script pergunta a senha do MySQL (usuário `root` por padrão). Para usar outro usuário ou servidor, defina antes as variáveis `MYSQL_USER`, `MYSQL_HOST` ou `MYSQL_PORT`.
   - Para rodar só uma etapa: `python python/etl/main.py --etapa tratar` (opções: `extrair`, `tratar`, `staging`, `mmd`, `dump`).
4. Ao final, os dumps ficam em `database/dumps/`. Se o `mysqldump` não for encontrado, o script avisa e os dumps podem ser gerados pelo MySQL Workbench em Server → Data Export.

## Scripts SQL usados na carga

- `database/ddl/03-criar-staging.sql`: cria o banco `staging_pib`
- `database/ddl/02-criar-tabelas-mysql.sql`: cria o banco `pib_municipios` (MMD) e as tabelas
- `database/etl/00-limpar-mmd.sql`: apaga o MMD para a carga poder ser repetida
- `database/etl/01` a `05`: carga das dimensões (região, UF, município, tempo) e da fato
- `database/etl/06-validacao-carga.sql`: conferência dos totais e dos registros órfãos
