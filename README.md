## 📊 TCC – Análise de Desinformação e COVID-19 com Séries Temporais

Este repositório contém o projeto de Trabalho de Conclusão de Curso (TCC) de Henrique Dias, focado na aplicação de modelagem de séries temporais para investigar a relação entre ondas de desinformação sobre a pandemia e a evolução dos casos de COVID-19 em Curitiba (2020-2023).

---

## 📌 Objetivo

	O objetivo central é quantificar se a inclusão de uma variável de desinformação melhora a acurácia de modelos preditivos para a curva de contágio da COVID-19.
	
	Os objetivos específicos incluem:
		-Coletar e estruturar dados de checagens falsas sobre a pandemia no site da Agência Lupa (2020–2023).
		-Preparar e tratar os dados epidemiológicos oficiais da COVID-19 para o município de Curitiba (SESA/PR).
		-Realizar uma análise exploratória para identificar tendências, sazonalidades e padrões visuais em ambas as séries temporais.
		-Conduzir uma competição de modelos estatísticos para avaliar o impacto da desinformação, comparando:
	  		-ARIMA: Modelo base univariado.
	  		-SARIMA: Modelo com componente sazonal.
	  		-ARIMAX: Modelo com a desinformação como variável exógena.
	  		-SARIMAX: Modelo combinado.
		-Discutir os resultados e as implicações da infodemia para a gestão da saúde pública.

---

## 🧰 Tecnologias e Bibliotecas

- Linguagem: Python 3.x
- Análise de Dados: pandas, numpy
- Visuaçização: matplotlib, seaborn
- Modelagem Estatística: statsmodels, pmdarima
- Métrica de Avaliação: scikit-learn (para testes de regressão)
- Coleta de Dados: requests
- Ambiente de Desenvolvimento: Jupyter Notebook ou VS Code

---

## 📁 Estrutura do Projeto

```bash
📂 tcc_infodemia_covid/
│
├── 📜 README.md
├── 📄 requirements.txt
├── 📁 dados/
│   ├── 📥 raw/
│   └── 📤 processed/
├── 📓 notebooks/
├── 📂 resultados/
│   ├── 📊 graficos/
│   └── 📈 tabelas/
└── 🐍 src/
