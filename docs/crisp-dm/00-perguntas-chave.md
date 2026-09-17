# 🎯 PROJETO BUSINESS INTELLIGENCE — PERGUNTAS-CHAVE E CONTEXTO (100%)

## Laboratório de Inovação IV — Prof. Edilberto Silva — 2026

---

## 👥 COMPOSIÇÃO DA EQUIPE

| ID | Nome Completo | Papel Primário | E-mail |
| :---: | :---- | :---- | :---- |
| 1 | Daniel Reis Rodrigues | Scrum Master / BI Lead / Analista de Dados | danielreisrodrigues15@gmail.com |
| 2 | Caio Nunes Lima | Engenheiro de Dados / Desenvolvedor Power BI | caionunes123@gmail.com |

> **Observação:** a equipe do projeto é formada por apenas 2 integrantes. Por isso, os papéis do modelo original foram agrupados entre os dois membros, em vez de manter uma equipe de 6 pessoas.

**Ambos os integrantes devem compreender:**

- ✅ A estrutura geral do projeto de BI
- ✅ O processo de tratamento e organização dos dados
- ✅ Os principais indicadores (KPIs) analisados
- ✅ Como os dados serão apresentados/visualizados

---

## 📊 IDENTIFICAÇÃO DO PROJETO

**Nome do Projeto:**
Análise do PIB dos Municípios Brasileiros (2010–2023)

**Descrição Executiva:**
Projeto de Business Intelligence que utiliza a base de dados do IBGE sobre o PIB dos municípios brasileiros para analisar a evolução do PIB entre 2010 e 2023 e comparar municípios, estados e regiões.

**Stakeholder Patrocinador:**
Prof. Edilberto Silva (professor da disciplina Laboratório de Inovação IV, responsável pela avaliação do projeto).

**Período de Execução:**
**

---

## 🎯 PERGUNTA-CHAVE (NORTEADORA) — 25%

### Pergunta Principal

**Qual é a pergunta estratégica que este BI vai responder?**

"Como o Produto Interno Bruto dos municípios brasileiros evoluiu entre 2010 e 2023 e quais municípios, estados e regiões apresentaram os maiores valores de PIB e PIB per capita?"

**Critérios da Pergunta:**

- ✅ **Específica:** foca na evolução do PIB e na comparação entre municípios, estados e regiões, não em "melhorar a economia" de forma genérica.
- ✅ **Mensurável:** pode ser respondida com valores de PIB e PIB per capita presentes na base.
- ✅ **Alinhada ao objetivo do trabalho:** organizar e analisar dados públicos do IBGE.
- ✅ **Viável:** é possível responder com os dados disponíveis na base "PIB dos Municípios - base de dados 2010-2023.xlsx".
- ✅ **Relevante:** gera informações úteis para entender desigualdades econômicas entre regiões do Brasil.

---

### Sub-Perguntas (Decomposição)

> **Observação:** o modelo original organiza as sub-perguntas em "operacional (diária)", "tática (semanal)", "estratégica (mensal)" e "preditiva (futura)". Como a base do IBGE é publicada anualmente (não em tempo real), essas categorias foram adaptadas para representar diferentes **níveis de análise** em vez de diferentes períodos de tempo.

**Pergunta 1 (Descritiva):**
Quais municípios apresentaram os maiores valores de PIB?

**Pergunta 2 (Comparativa):**
Quais estados e regiões concentram os maiores valores de PIB?

**Pergunta 3 (Evolutiva):**
Como o PIB dos municípios evoluiu ao longo dos anos (2010 a 2023)?

**Pergunta 4 (Per Capita):**
Quais municípios apresentaram os maiores valores de PIB per capita?

---

## 📖 STORYTELLING — NARRATIVA DO PROJETO — 30%

### Cenário AS-IS (Situação Atual — Problema)

**Contexto:**

O IBGE disponibiliza uma grande quantidade de informações sobre o PIB dos municípios brasileiros, cobrindo o período de 2010 a 2023. A base possui dados de milhares de municípios, distribuídos entre diferentes anos e indicadores econômicos.

O problema é que essa grande quantidade de informações torna a análise manual mais trabalhosa. Sem uma organização adequada, é difícil identificar rapidamente quais municípios possuem os maiores PIBs, comparar estados e regiões entre si e observar como o PIB evoluiu ao longo do tempo.

**Dores Principais:**

- 📌 Dificuldade de identificar rapidamente os municípios com maior PIB e maior PIB per capita em meio a mais de 77 mil registros.
- 📌 Dificuldade de comparar estados e regiões de forma organizada.
- 📌 Falta de uma visão clara da evolução do PIB ao longo dos anos (2010–2023).

---

### Transição (Mudança — Transformação)

**O que será feito para chegar ao resultado desejado:**

Organizar e tratar os dados da base do IBGE, selecionando os campos necessários para a análise, principalmente:

- Ano
- Região
- Estado (UF)
- Município
- PIB (a preços correntes)
- PIB per capita

Depois disso, serão realizadas comparações entre anos, municípios, estados e regiões, e os dados serão preparados para visualização (por exemplo, em gráficos e/ou dashboard).

**⚠️ Limitação importante da base:** para os anos de 2022 e 2023, o IBGE disponibilizou apenas o PIB e o PIB per capita — os dados por setor econômico (Agropecuária, Indústria, Serviços etc.) não foram divulgados para esses dois anos. Por isso, análises setoriais serão feitas apenas com o período de 2010 a 2021, enquanto o PIB total e o PIB per capita podem ser analisados no período completo (2010–2023).

### Cenário TO-BE (Resultado Esperado)

Ao final do projeto, teremos uma estrutura organizada que permita analisar de forma simples a evolução do PIB dos municípios brasileiros entre 2010 e 2023. O resultado deverá facilitar:

- a identificação dos municípios com maiores PIBs;
- a comparação entre estados;
- a comparação entre as cinco grandes regiões do Brasil;
- a análise do PIB per capita;
- a visualização da evolução do PIB ao longo dos anos.

---

## 📊 FONTES DE DADOS E INFORMAÇÕES — 25%

### Tabela Consolidada de Fontes

| ID | Sistema/Fonte | Tipo | URL/Localização | Frequência | Volume | Contato |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| F-01 | PIB dos Municípios (IBGE) | Arquivo Excel (.xlsx) | https://ftp.ibge.gov.br/Pib_Municipios/2022_2023/base/ | Anual (publicação do IBGE) | 77.965 registros / 43 campos | IBGE (não há contato individual — dado público) |

---

### Descrição Técnica — Cada Fonte

#### **F-01: PIB dos Municípios — IBGE (Excel)**

**Sobre o arquivo:**

Nome do arquivo: PIB dos Municípios - base de dados 2010-2023.xlsx
Página oficial da pesquisa: https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html
Diretório de download: https://ftp.ibge.gov.br/Pib_Municipios/2022_2023/base/
Período coberto: 2010 a 2023

**Abas (planilhas) do arquivo:**

- `PIB dos Municípios` → aba principal, com 77.965 registros e 43 campos.
- `Notas` → notas técnicas do IBGE sobre a construção dos dados (inclui a observação sobre a limitação de 2022 e 2023).

**Principais campos utilizados neste projeto:**

| Campo | Tipo | Descrição |
| :---- | :---- | :---- |
| Ano | Numérico | Ano de referência do dado econômico. |
| Nome da Grande Região | Texto | Região do Brasil onde o município está localizado. |
| Sigla da Unidade da Federação | Texto | Sigla do estado onde o município está localizado. |
| Nome da Unidade da Federação | Texto | Nome do estado onde o município está localizado. |
| Código do Município | Numérico | Código utilizado para identificar o município. |
| Nome do Município | Texto | Nome do município analisado. |
| Produto Interno Bruto, a preços correntes (R$ 1.000) | Numérico | Valor do PIB do município no ano analisado, em milhares de reais. |
| Produto Interno Bruto per capita, a preços correntes (R$ 1,00) | Numérico | Valor do PIB do município dividido pela população. |

> A base original possui outros campos (ex.: Valor Adicionado Bruto por setor — Agropecuária, Indústria, Serviços, Administração Pública), que também podem ser usados de forma complementar, respeitando a limitação de dados setoriais indisponíveis para 2022 e 2023.

**Frequência de atualização:** o IBGE publica esta base anualmente (dado histórico, não em tempo real).

**Contato de suporte:** não se aplica — trata-se de uma base pública disponibilizada pelo IBGE, sem contato individual de suporte.

---

## 📁 ESTRUTURA DE DIRETÓRIOS — REPOSITÓRIO GITHUB — 10%

### Repositório GitHub

URL Principal: *https://github.com/DanielNego/projeto-bi-pib-municipios.git*
Proprietário: Daniel Reis Rodrigues e Caio Nunes Lima
Visibilidade: Público


```
projeto-bi-pib-municipios/
│
├── README.md                          ← Apresentação do projeto
│
├── docs/
│   └── crisp-dm/
│       ├── 00-perguntas-chave.md      ← Este arquivo (Fase 0)
│       ├── 01-business-understanding.md   ← Fase 1
│       ├── 02-data-understanding.md       ← Fase 2
│       ├── 03-data-preparation.md         ← Fase 3
│       ├── 04-modeling.md                 ← Fase 4
│       ├── 05-evaluation.md               ← Fase 5
│       └── 06-deployment.md               ← Fase 6
│
├── dados/
│   └── PIB dos Municípios - base de dados 2010-2023.xlsx
│
└── power-bi/
    └── projeto-pib-municipios.pbix    ← Adicionado quando o dashboard estiver pronto
```

Novas pastas (por exemplo, para scripts de tratamento de dados) serão criadas somente quando forem realmente utilizadas.

---

## 🤖 USO DE IA PARA CRIAR MÉTRICAS E TRATAR DADOS — 10%

### Assistentes de IA Utilizados

Foram utilizadas IAs (ChatGPT e Claude) como apoio no projeto, principalmente para ajudar a definir perguntas, métricas, organização e interpretação dos dados. A IA não realizou toda a análise dos dados — o tratamento dos dados em si é feito pela equipe.

**Prompt utilizado como evidência:**

"Com base em uma base do IBGE sobre PIB dos Municípios de 2010 a 2023, contendo ano, região, estado, município, PIB e PIB per capita, sugira métricas que ajudem a responder uma pergunta sobre a evolução do PIB e a comparação entre municípios, estados e regiões."

**Métricas sugeridas pela IA e adotadas no projeto:**

**1. PIB total**
Objetivo: analisar o valor do PIB dos municípios em cada ano e comparar municípios, estados e regiões.

**2. PIB per capita**
Objetivo: analisar o PIB considerando a população do município.

**3. Crescimento do PIB**
Objetivo: verificar a variação percentual do PIB entre dois períodos.
Fórmula: Crescimento (%) = ((PIB atual − PIB anterior) / PIB anterior) × 100

**4. Ranking de municípios**
Objetivo: identificar os municípios com maiores valores de PIB e PIB per capita.

**5. PIB por região**
Objetivo: comparar o PIB das cinco grandes regiões brasileiras (Norte, Nordeste, Centro-Oeste, Sudeste e Sul).

---

## ✅ PRÓXIMAS ETAPAS

**Após completar este documento (Fase 00):**

1. ✅ Planejar a **Fase 1:** `01-business-understanding.md` (100%)

---

**Documento Criado:** 
**Versão:** 1.0
**Status:**

*"Bom BI começa com perguntas certas!"* 🎯

Prof. Edilberto Silva - FACSENAC - v.1.set.26
