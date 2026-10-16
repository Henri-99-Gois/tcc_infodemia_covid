## TCC – Modelagem de Séries Temporais com Variáveis de Desinformação: O Caso da COVID-19 em Curitiba

Este repositório contém os scripts e os dados do Trabalho de Conclusão de Curso (TCC) do bacharelado em Gestão da Informação (UFPR), desenvolvido por Henrique Gois Dias. O projeto compara, semana a semana, os casos confirmados de COVID-19 em Curitiba com o número de checagens de conteúdo falso publicadas pela Agência Lupa, de 2020 a 2022.

---

## Objetivo

Investigar se há relação temporal entre o volume de checagens de desinformação e a evolução dos casos de COVID-19 em Curitiba.

O código:

- coleta as checagens com selo "Falso" da Agência Lupa;
- filtra os microdados da SESA/PR para Curitiba e agrega casos e checagens em séries semanais;
- aplica o teste Dickey-Fuller Aumentado (ADF), a função de correlação cruzada (CCF) e o teste de causalidade de Granger.

---

## Tecnologias e Bibliotecas

- Linguagem: Python 3.11
- Coleta de dados: requests
- Manipulação de dados: pandas, numpy
- Estatística: statsmodels (ADF, CCF, Granger)
- Visualização: matplotlib
- Ambiente: VS Code / Jupyter Notebook

---

## Estrutura do Projeto

```bash
tcc_infodemia_covid/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/          # bases originais (baixar pelo Drive)
│   ├── intermediate/ # casos diários de Curitiba
│   └── processed/    # série semanal unificada
├── notebooks/        # 01 → 02 → 02b → 03
├── results/
│   ├── figures/      # Figuras 2 a 5 do TCC
│   └── tables/       # Tabelas 1 e 2 do TCC
└── archive/          # tentativas anteriores com ARIMA/ARIMAX
```

---

## Dados

As bases originais estão no Google Drive, porque a da SESA tem 375 MB: **[pasta `raw`](https://drive.google.com/drive/folders/16IV_BZpdE3glv4XNhQ5VprCZL_yiZpxE?usp=sharing)**. Baixe os dois arquivos para `data/raw/`.

| Arquivo | Fonte | MD5 |
|---|---|---|
| `casos_covid_parana_raw.csv` | SESA/PR, [Informe Epidemiológico de 17/01/2024, CSV "Geral"](https://www.documentador.pr.gov.br/documentador/pub.do?action=d&uuid=@gtf-escriba-sesa@a578e8e6-26aa-4327-90ca-a1ce0887c40c) | `113d7271e9dbaf4ac168ceaaa2c78881` |
| `checagens_lupa_raw.csv` | Agência Lupa, checagens com selo "Falso" coletadas em maio/2025 (notebook 01) | `78f313f015531011ecb468d4a1ccb5e7` |

> O serviço de busca usado na coleta da Lupa foi desativado, então a coleta não pode ser refeita. O CSV é o registro original.

---

## Como reproduzir

```bash
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Execute os notebooks a partir da pasta `notebooks/`, nesta ordem:

| Notebook | Gera |
|---|---|
| `01_coleta_dados` | confere os totais da Lupa (a célula de coleta **não** precisa ser executada) |
| `02_analise_exploratoria_e_preprocessamento` | `data/intermediate/casos_diarios_curitiba.csv`, Figuras 2 e 3 |
| `02b_agregacao_semanal_e_unificacao` | `data/processed/series_semanais_curitiba.csv` |
| `03_correlacao_causalidade` | Figuras 4 e 5, Tabelas 1 (ADF) e 2 (Granger) |

Os arquivos saem em `results/figures/` e `results/tables/`, com o número correspondente no TCC (por exemplo, `figura4_...png`, `tabela2_granger.csv`).
