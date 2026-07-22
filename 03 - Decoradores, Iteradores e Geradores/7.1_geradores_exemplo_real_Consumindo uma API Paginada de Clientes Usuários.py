import time
import requests


def buscar_usuarios_api_paginada(limite_por_pagina=2, max_paginas=3):
    """
    Gerador que faz requisições paginadas a uma API e entrega (yield)
    um usuário de cada vez para o código principal.
    
    """
    pagina_atual = 1

    while pagina_atual <= max_paginas:
        url = f"https://jsonplaceholder.typicode.com/users?_page={pagina_atual}&_limit={limite_por_pagina}"

        print(f"\n🌐 [API] Requisitando a página {pagina_atual}...")
        resposta = requests.get(url)

        if resposta.status_status_code != 200 if hasattr(resposta, 'status_status_code') else resposta.status_code != 200:
            print("❌ Erro ao buscar dados da API.")
            break

        dados = resposta.json()

        # Se a API não retornar mais dados, encerramos a busca
        if not dados:
            print("🏁 Fim dos dados na API.")
            break

        # Entrega CADA usuário individualmente via yield
        for usuario in dados:
            yield {
                "id": usuario["id"],
                "nome": usuario["name"],
                "email": usuario["email"],
                "empresa": usuario["company"]["name"],
            }

        pagina_atual += 1
        time.sleep(1)  # Boa prática: evita sobrecarregar o servidor remoto


# --- CONSUMINDO O GERADOR NO DIA A DIA ---

print("------ Iniciando o processamento via Gerador (Lazy Loading) ------")

# O gerador NÃO faz todas as requisições de uma vez aqui!
gerador_usuarios = buscar_usuarios_api_paginada(limite_por_pagina=2, max_paginas=3)

# A requisição só é disparada conforme o loop pede o próximo item
for usuario in gerador_usuarios:
    print(
        f"👤 Usuário #{usuario['id']}: {usuario['nome']} | "
        f"Email: {usuario['email']} | Empresa: {usuario['empresa']}"
    )