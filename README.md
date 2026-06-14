## 📊 TCC – Modelagem de Séries Temporais com Variáveis de Desinformação: O Caso da COVID-19 em Curitiba

Este repositório contém os scripts e rotinas de dados do Trabalho de Conclusão de Curso (TCC) do bacharelado em Gestão da Informação (UFPR) desenvolvido por Henrique Dias. O projeto aplica engenharia de dados e modelagem econométrica de séries temporais para investigar a relação de precedência temporal entre o fluxo de desinformação digital (fake news) e o agravamento das curvas de contágio da COVID-19 no município de Curitiba (Recorte: 2020 a 2022).

---

## 📌 Objetivo

	O objetivo central da pesquisa é quantificar o impacto da "infodemia" na saúde pública, provando matematicamente o tempo de latência entre as ondas de desinformação e o consequente colapso do sistema de saúde, utilizando testes avançados de causalidade para descartar relações espúrias.
	
	Os objetivos específicos e metodológicos incluem:
		-Extração via API: Coletar e estruturar dados de checagens com selo "Falso" na plataforma da Agência Lupa.
		-Engenharia de Dados: Filtrar microdados estaduais (SESA/PR), isolar a capital e agregar milhares de notificações diárias em um dataset unificado de Semanas Epidemiológicas.
		-Análise Exploratória: Aplicar Média Móvel (MM7) e Decomposição Sazonal (STL) para tratamento de ruídos diários e represamentos administrativos em hospitais.
		-Modelagem Econométrica Multivariada:
			-Aplicação do Teste Dickey-Fuller Aumentado (ADF) para garantir estacionariedade (I(0)).
			-Uso da Função de Correlação Cruzada (CCF) para mapear o lag ótimo de impacto (identificando um atraso de 42 dias).
			-Execução do Teste de Causalidade de Granger bidirecional em ambiente VAR (Vector Autoregression) para descartar a bicausalidade e provar a precedência unidirecional da desinformação.

---

## 🧰 Tecnologias e Bibliotecas

- Linguagem: Python 3.x
- Coleta de Dados: requests, time
- Manipulação e Engenharia de Dados: pandas, numpy
- Modelagem Estatística: statsmodels (Testes ADF, CCF, VAR, Granger e Decomposição STL)
- Visualização de Dados: matplotlib (com estilo seaborn-whitegrid)
- Ambiente de Desenvolvimento: Visual Studio Code / Jupyter Notebook

---

## 📁 Estrutura do Projeto

```bash
📂 tcc_infodemia_covid/
│
├── 📜 README.md
├── 📄 requirements.txt
│ 
├── 📁 dados/
│   ├── 📥 raw/
│   └── 📤 processed/
│ 
├── 📓 notebooks/
│    ├── 01_coleta_dados
│    ├── 02_analise_exploratoria_e_preprocessamento
│    ├── 02b_agregacao_semanal_e_unificacao
│    └── 03_correlacao_causalidade
│ 
└── 📂 resultados/
    ├── 📊 graficos/
    └── 📈 tabelas/
 
