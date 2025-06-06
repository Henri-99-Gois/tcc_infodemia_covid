📊 TCC – Modelos Estatísticos Aplicados à COVID-19 em Curitiba

Este repositório contém o projeto de Trabalho de Conclusão de Curso (TCC) de Henrique Dias, com foco na aplicação de **modelos estatísticos para análise e previsão da evolução da COVID-19**, utilizando dados reais de Curitiba.

---

## 📌 Objetivo

- Analisar a evolução dos casos e mortes por COVID-19 com base em séries temporais reais
- Comparar o desempenho de diferentes modelos estatísticos, como **médias móveis, suavização exponencial e SARIMA**
- Simular cenários de incerteza usando **Monte Carlo**
- Investigar correlação entre os dados e variáveis externas (como períodos de fake news ou políticas públicas)
- Gerar insights que possam ser úteis para planejamento e políticas de saúde

---

## 🧰 Tecnologias e Bibliotecas

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- statsmodels (SARIMA, ETS)
- scikit-learn (para testes de regressão)
- `random` + `simpy` (para simulação Monte Carlo)
- Jupyter Notebook ou VS Code

---

## 📁 Estrutura do Projeto

```bash
📂 tcc_covid_curitiba/
│
├── dados/
│   └── covid_curitiba.csv
│
├── notebooks/
│   ├── 01_analise_exploratoria.ipynb
│   ├── 02_modelos_sarima.ipynb
│   ├── 03_simulacao_montecarlo.ipynb
│   └── 04_visualizacoes_finais.ipynb
│
├── src/
│   └── funcoes_utilitarias.py
│
├── README.md
└── requirements.txt
