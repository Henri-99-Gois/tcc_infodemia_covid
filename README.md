# 🧠 Análise Linguística e Sentimental de Reclamações – NLP com Python

Este projeto utiliza **Python + spaCy + TF-IDF** para realizar uma análise textual completa de reclamações de consumidores, aplicando técnicas de **Processamento de Linguagem Natural (PLN)** e classificação de sentimento.

============================================================================================

## 📌 Objetivo

- Extrair informações estruturadas de textos soltos (tokenização, POS, entidades nomeadas)
- Aplicar **tagueamento personalizado** com base em domínio específico
- Classificar **sentimento com regras simples**
- Identificar palavras relevantes via **TF-IDF**
- Gerar arquivos `.csv` para visualização ou análise posterior

============================================================================================

## 🧰 Tecnologias e Bibliotecas

- Python 3.10+
- spaCy (`pt_core_news_sm`)
- pandas
- scikit-learn (TF-IDF)
- Jupyter ou VS Code

============================================================================================

## 🧪 O que o script faz

1. Tokeniza cada frase, aplica POS tagging e dependência gramatical
2. Detecta **Entidades Nomeadas** (NER) como datas, locais e pessoas
3. Aplica um **sistema de "Custom Tags"** por palavra (produto, entrega, problema, etc.)
4. Classifica sentimento por **regras manuais**
5. Calcula TF-IDF para identificar palavras mais relevantes
6. Exporta os seguintes arquivos:

```text
✅ analise_linguistica_5frases.csv
✅ sentimento_reclamacoes.csv
✅ tfidf_reclamacoes.csv
