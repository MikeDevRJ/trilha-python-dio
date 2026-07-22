import requests


def fetch_products(max_pages=3):
    page = 1
    limit = 5  # Traz 5 produtos por página
    
    while page <= max_pages:
        skip = (page - 1) * limit
        url = f"https://dummyjson.com/products?limit={limit}&skip={skip}"
        
        print(f"\n🌐 [API] Buscando página {page}...")
        response = requests.get(url)
        data = response.json()
        
        # O 'yield' entrega um produto por vez para quem chamou a função
        for product in data['products']:
            yield product
            
        # Se a quantidade de itens buscados atingir o total da API, paramos
        if skip + limit >= data['total']:
            break
            
        page += 1


# --- Chamada e consumo do gerador ---
print("--- Iniciando busca de produtos via Gerador ---")

for product in fetch_products(max_pages=2):
    print(f"📦 Produto #{product['id']}: {product['title']} | Preço: ${product['price']}")