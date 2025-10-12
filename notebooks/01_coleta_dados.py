# --------------------------------------------------------------------- 
# 1. Importar bibliotecas essenciais 
# --------------------------------------------------------------------- 
import requests         
# Requisições HTTP para acessar a API da Lupa 
import time              
import csv               
# Controle de tempo entre as requisições 
# Exportação dos dados para arquivo CSV 

# --------------------------------------------------------------------- 
# 2. Configurar URL e cabeçalhos da API da Lupa 
# --------------------------------------------------------------------- 
URL = "https://api.lupa.news/api/v1/search" 
HEADERS = { 
"Content-Type": "application/json", 
"Origin": "https://lupa.uol.com.br", 
"Referer": "https://lupa.uol.com.br/", 
"User-Agent": "Mozilla/5.0" 
} 

# --------------------------------------------------------------------- 
# 3. Definir palavras-chave de interesse 
# --------------------------------------------------------------------- 
palavras_chave = [ 
"vacina", "antivacina", "vacinação obrigatória", 
"cloroquina", "ivermectina", "tratamento precoce", 
"chip vacina", "bill gates", "5G", "nova ordem mundial", 
"COVID é mentira", "coronavírus não existe", "morte inventada", 
"STF covid", "OMS", "médico denuncia", "Doria covid", "Bolsonaro covid", 
"fake news", "desinformação", "boato", "notícia falsa" 
]
 
# --------------------------------------------------------------------- 
# 4. Definir parâmetros de paginação da API 
31 
# --------------------------------------------------------------------- 
LIMITE_PAGINAS = 50       
# Número máximo de páginas por termo 
POR_PAGINA = 10           
# Resultados por página (offset) 

# --------------------------------------------------------------------- 
# 5. Lista principal para armazenar os dados coletados 
# --------------------------------------------------------------------- 
todos_resultados = [] 

# --------------------------------------------------------------------- 
# 6. Função para buscar dados com base em uma palavra-chave 
# --------------------------------------------------------------------- 
def buscar_lupa(palavra): 
resultados = [] 
for pagina in range(LIMITE_PAGINAS): 
offset = pagina * POR_PAGINA 
payload = { 
"query": palavra, 
"tags": ["Falso"], 
"sort": ["published_at", "desc"], 
"types": [], 
"categories": [], 
"startDate": "2020-01-01T00:00:01.000Z", 
"endDate": "2023-12-31T23:59:59.999Z", 
"from": offset 
} 
response = requests.post(URL, headers=HEADERS, json=payload) 
if response.status_code != 200: 
print(f"Página 
{pagina+1} da palavra-chave '{palavra}' falhou. Código:", 
response.status_code) 
break 
data = response.json() 
hits = data.get("hits", []) 
if not hits: 
print(f"Fim dos resultados para '{palavra}'.") 
break 
for item in hits: 
32 
resultados.append({ 
"titulo": item.get("name"), 
"url": "https://lupa.uol.com.br/" + item.get("full_slug"), 
"data_publicacao": item.get("published_at") 
}) 
print(f"Página {pagina+1} de '{palavra}' finalizada com sucesso.") 
time.sleep(1)  # Evita sobrecarga no servidor 
return resultados
 
# --------------------------------------------------------------------- 
# 7. Executar busca para cada palavra-chave e acumular resultados 
# --------------------------------------------------------------------- 
for palavra in palavras_chave: 
print(f"\nIniciando busca por '{palavra}'...") 
resultados = buscar_lupa(palavra) 
todos_resultados.extend(resultados) 

# --------------------------------------------------------------------- 
# 8. Eliminar duplicatas com base na URL 
# --------------------------------------------------------------------- 
unicos = {item['url']: item for item in todos_resultados} 
lista_final = list(unicos.values())
 
# --------------------------------------------------------------------- 
# 9. Exportar resultados finais para arquivo CSV 
# --------------------------------------------------------------------- 
output_path = "H:/Writings/TCC I/code/checagens_lupa_completo.csv" 
with open(output_path, mode='w', newline='', encoding='utf-8') as csvfile: 
campos = ["titulo", "url", "data_publicacao"] 
writer = csv.DictWriter(csvfile, fieldnames=campos) 
writer.writeheader() 
writer.writerows(lista_final) 

# --------------------------------------------------------------------- 
# 10. Mensagem final de conclusão 
# --------------------------------------------------------------------- 
print(f"\nBUSCA CONCLUÍDA: {len(lista_final)} registros únicos salvos em '{output_path}'") 
# ---------------------------------------------------------------------