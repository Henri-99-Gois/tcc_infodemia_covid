# -----------------------------------------------------------
# 1. Importar bibliotecas essenciais
# -----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL       # <-- novo import

# -----------------------------------------------------------
# 2. Carregar o arquivo CSV (seu caminho já definido)
# -----------------------------------------------------------
caminho_arquivo = r'H:\Writings\TCC I\INFORME_EPIDEMIOLOGICO_17_01_2024_GERAL.csv'
df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1')

# -----------------------------------------------------------
# 3. Filtro e pré-processamento de Curitiba
# -----------------------------------------------------------
df_curitiba = df[df['MUN_RESIDENCIA'].str.upper() == 'CURITIBA'].copy()
df_curitiba['DATA_DIAGNOSTICO'] = pd.to_datetime(df_curitiba['DATA_DIAGNOSTICO'],
                                                 errors='coerce')

casos_por_dia = df_curitiba.groupby('DATA_DIAGNOSTICO').size()

# -----------------------------------------------------------
# 4. SUAVIZAÇÃO 1 – Média móvel de 7 dias
# -----------------------------------------------------------
casos_mm7 = casos_por_dia.rolling(window=7, center=True).mean()

# Gráfico comparando série bruta x média móvel
plt.figure(figsize=(14, 6))
plt.plot(casos_por_dia, label='Casos diários brutos', alpha=0.4)
plt.plot(casos_mm7,   label='Média móvel 7 dias', linewidth=2)
plt.title('Casos confirmados de COVID-19 – Curitiba (Original x MM7)')
plt.xlabel('Data')
plt.ylabel('Número de casos')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# 5. SUAVIZAÇÃO 2 – STL Decomposition
# -----------------------------------------------------------
# Força frequência diária para o STL
casos_stl = casos_por_dia.asfreq('D')

stl = STL(casos_stl, period=7, robust=True)
resultado = stl.fit()

tendencia  = resultado.trend
sazonal    = resultado.seasonal
residuo    = resultado.resid

# Plotar componentes
fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)
casos_stl.plot(ax=axes[0], color='gray', label='Original')
axes[0].set_title('Série original'); axes[0].grid(True)

tendencia.plot(ax=axes[1], color='blue', label='Tendência')
axes[1].set_title('Tendência (STL)'); axes[1].grid(True)

sazonal.plot(ax=axes[2], color='green', label='Sazonalidade semanal')
axes[2].set_title('Sazonalidade (STL)'); axes[2].grid(True)

residuo.plot(ax=axes[3], color='red', label='Resíduo')
axes[3].set_title('Resíduo'); axes[3].grid(True)

plt.tight_layout()
plt.show()

# -----------------------------------------------------------
# 6. (Opcional) Exportar componentes para análise posterior
# -----------------------------------------------------------
componentes = pd.concat([tendencia, sazonal, residuo], axis=1)
componentes.columns = ['tendencia', 'sazonal', 'residuo']
componentes.to_csv('componentes_stl_curitiba.csv', index=True)
