# Instalar o pacote poetry
# pip install poetry

# 1. Iniciar um projeto novo
# poetry new meu-projeto

"""]
O comando poetry init cria um arquivo de configuração pyproject.toml interativo para um projeto que já existe (ou em uma pasta já criada).
Em vez de criar uma estrutura inteira do zero com pastas e arquivos de código (como faz o poetry new), o init faz um "questionário" no seu terminal para gerar a estrutura base de dependências do seu projeto.


poetry init


Depois de rodar o poetry init, execute o comando poetry install para que o Poetry crie o
ambiente virtual (.venv) e instale todas as dependências listadas.


poetry install

poetry show -t

poetry remove django

# 2. Adicionar uma biblioteca (cria o .venv e instala)poe
poetry add requestspo

# 3. Rodar um script dentro do ambiente virtual do Poetry
poetry run python main.py

# 4. Entrar no terminal do ambiente virtual
poetry shell

"""
