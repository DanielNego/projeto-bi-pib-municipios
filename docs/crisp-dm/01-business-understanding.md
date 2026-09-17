# FASE 1: COMPREENSÃO DO NEGÓCIO

## Laboratório de Inovação IV — Prof. Edilberto Silva — 2026

**Projeto:** Análise do PIB dos Municípios Brasileiros (2010–2023)
**Grupo:** grupo03 — PIB Municípios
**Localização dos Arquivos:** https://github.com/DanielNego/projeto-bi-pib-municipios/blob/main/docs/crisp-dm/01-business-understanding.md
**Repositório GitHub:** https://github.com/DanielNego/projeto-bi-pib-municipios.git
**Data:** *17/09/2026*
**Última Atualização:** *17/09/2026*
**Status:** EM DESENVOLVIMENTO

---

## 1. CONTEXTO ORGANIZACIONAL — 5%

**Organização/Departamento:**
IBGE (Instituto Brasileiro de Geografia e Estatística), órgão vinculado ao Ministério do Planejamento e Orçamento (MPO). Para efeito deste projeto acadêmico, consideramos o IBGE/MPO como a "organização" para a qual o BI estaria sendo desenvolvido, já que é o próprio IBGE quem produz e disponibiliza a base de dados do PIB dos Municípios.

**Situação Atual:**
O IBGE disponibiliza os dados de PIB dos municípios em uma planilha grande (77.965 registros e 43 campos, cobrindo 2010 a 2023), publicada de forma bruta (Excel), sem comparações prontas entre municípios, estados e regiões, nem visualizações que facilitem a leitura para quem consulta os dados — seja o público em geral, pesquisadores, gestores públicos ou imprensa.

**Problema/Oportunidade:**
A oportunidade é organizar e tratar esses dados para responder, de forma clara, como o PIB dos municípios evoluiu entre 2010 e 2023 e quais municípios, estados e regiões se destacam em PIB e PIB per capita — facilitando o acesso a essa informação para quem usa os dados do IBGE, algo que hoje exigiria bastante trabalho manual na planilha bruta.

---

## 2. OBJETIVOS DE NEGÓCIO (OKRs) — 20%

**Objetivo Principal:**
Organizar e analisar os dados de PIB dos municípios brasileiros (2010–2023) para identificar padrões de evolução econômica e comparar municípios, estados e regiões.

| ID     | Objetivo                                                                      | KPI de Sucesso                                                                                                 | Prazo        |
|:------ |:----------------------------------------------------------------------------- |:-------------------------------------------------------------------------------------------------------------- |:------------ |
| OBJ-01 | Tratar e organizar a base de dados do IBGE                                    | Base limpa com os campos principais (ano, região, estado, município, PIB, PIB per capita) prontos para análise | *30/09/2026* |
| OBJ-02 | Identificar os municípios, estados e regiões com maiores PIB e PIB per capita | Ranking dos 10 maiores municípios em PIB e em PIB per capita                                                   | *15/10/2026* |
| OBJ-03 | Visualizar a evolução do PIB ao longo dos anos                                | Gráfico/dashboard mostrando a evolução do PIB de 2010 a 2023                                                   | *30/10/2026* |

---

## 3. ATORES E STAKEHOLDERS — 15%

| Ator                                                | Papel                                        | Necessidade Principal                                                                 |
|:--------------------------------------------------- |:-------------------------------------------- |:------------------------------------------------------------------------------------- |
| IBGE / Ministério do Planejamento e Orçamento (MPO) | Organização/fonte dos dados                  | Que os dados que produz e publica sejam usados de forma correta, sem distorções       |
| Prof. Edilberto Silva                               | Avaliador do projeto                         | Verificar se o projeto responde à pergunta-chave com dados corretos e bem organizados |
| Daniel Reis Rodrigues                               | Scrum Master / BI Lead / Analista de Dados   | Acompanhar o andamento do projeto e analisar os dados                                 |
| Caio Nunes Lima                                     | Engenheiro de Dados / Desenvolvedor Power BI | Tratar a base de dados e construir as visualizações                                   |

---

## 4. DEFINIÇÃO DO ESCOPO — 25%

**O que será incluso:**

- [x] Tratar a base de dados
- [x] PIB total dos municípios brasileiros (2010–2023)
- [x] PIB per capita dos municípios brasileiros (2010–2023)
- [x] Comparação entre municípios, estados e as 5 grandes regiões do Brasil
- [x] Evolução do PIB ao longo dos anos

**O que NÃO será incluso (fora do escopo):**

- [ ] Análise por setor econômico (Agropecuária, Indústria, Serviços) para 2022 e 2023, pois o IBGE não disponibilizou esses dados para esses dois anos
- [ ] Dados de outras fontes além do IBGE (ex.: dados populacionais adicionais, indicadores sociais)
- [ ] Previsão/projeção de PIB para anos futuros (o projeto é descritivo, não preditivo)

---

## 5. CRITÉRIOS DE SUCESSO — 20%

- ✅ Conseguir listar os municípios, estados e regiões com maiores valores de PIB e PIB per capita
- ✅ Conseguir mostrar de forma clara (gráfico ou dashboard) a evolução do PIB entre 2010 e 2023
- ✅ Entregar todas as fases do projeto (documentos e, quando aplicável, o Power BI) organizadas no repositório GitHub, dentro do prazo definido pela disciplina

---

## 6. RESTRIÇÕES E RISCOS — 15%

**Restrições Técnicas:**

- Para 2022 e 2023, a base do IBGE só traz PIB e PIB per capita (sem os dados por setor econômico), o que limita comparações setoriais a 2010–2021.
- A equipe é formada por apenas 2 integrantes, o que limita a quantidade de análises que podem ser feitas no prazo da disciplina.

**Riscos Identificados:**

| Risco                                                                        | Probabilidade | Impacto | Mitigação                                                                                      |
|:---------------------------------------------------------------------------- |:------------- |:------- |:---------------------------------------------------------------------------------------------- |
| Prazo curto para entregar todas as fases do CRISP-DM                         | ALTA          | ALTO    | Priorizar as métricas principais (PIB total, PIB per capita, ranking) antes de análises extras |
| Confusão entre dados de 2022/2023 (sem setores) e anos anteriores            | MÉDIA         | MÉDIO   | Deixar claro em todas as análises setoriais que o período considerado é 2010–2021              |
| Arquivo de dados grande (mais de 20 MB) dificultar o versionamento no GitHub | BAIXA         | BAIXO   | Confirmar que o upload no GitHub foi concluído corretamente na pasta `dados/`                  |

---

**Aprovado por:** *[Preencher — normalmente o professor, na correção]*
**Data de Aprovação:** *17/09/2026*

Prof. Edilberto Silva

Fé, Força e Foco


