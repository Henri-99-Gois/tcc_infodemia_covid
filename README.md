## 📊 TCC – Análise de Desinformação e COVID-19 com Séries Temporais

Este repositório contém o projeto de Trabalho de Conclusão de Curso (TCC) de Henrique Dias, com foco na aplicação de modelos estatísticos e análise de séries temporais para investigar a relação entre desinformação sobre vacinas e a evolução da COVID-19 no Brasil, com estudo de caso em Curitiba.

---

## 📌 Objetivo

- Coletar e estruturar dados de checagens falsas sobre vacinas no site da Agência Lupa (2020–2023)
- Coletar e preparar dados epidemiológicos oficiais da COVID-19 em Curitiba
- Analisar a evolução temporal de ambos os fenômenos (casos e fake news)
- Aplicar modelos estatísticos como:
  - Média móvel
  - Suavização exponencial
  - SARIMA e variações (SARIMAX/ARIMAX)
- Discutir correlações e possíveis implicações para políticas públicas de saúde

---

## 🧰 Tecnologias e Bibliotecas

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- statsmodels (SARIMA, ETS, ARIMAX)
- scikit-learn (para testes de regressão)
- selenium, requests, GraphQL (coleta de dados)
- Jupyter Notebook ou VS Code

---

## 📁 Estrutura do Projeto

```bash
📂 tcc_infodemia_covid/
├── 📁 dados/
│   ├── 📥 raw/
│   └── 📤 processed/
├── 📓 notebooks/
├── 📂 resultados/
│   ├── 📊 graficos/
│   └── 📈 tabelas/
└── 🐍 src/
