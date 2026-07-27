import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# Demonstração da forma incorreta de concatenação de strings que
# deixa o banco vulnerável. Ex.: digitar por exemplo 1 OR 1=1
id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
