import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

# conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
# print(conexao)


# Usando o 'with' para garantir o fechamento automático
# with sqlite3.connect(ROOT_PATH / "clientes.db") as conexao:
#    print(conexao)

# ROOT_PATH = Path(__file__).parent
db_path = ROOT_PATH / "clientes.db"

try:
    # O 'with' gerencia o contexto da conexão
    with sqlite3.connect(db_path) as conexao:
        # Cria um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Executa uma query simples que não altera o banco
        cursor.execute("SELECT sqlite_version();")

        # Recupera o resultado da query
        versao = cursor.fetchone()

        print(f"✅ Conexão bem-sucedida! Versão do SQLite: {versao[0]}")

except sqlite3.Error as e:
    print(f"❌ Erro ao conectar ao banco de dados: {e}")
