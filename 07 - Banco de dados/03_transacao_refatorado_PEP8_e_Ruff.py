import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
conexao.row_factory = sqlite3.Row


"""
No módulo sqlite3 do Python, a própria conexão funciona como um context manager: ela
gerencia a transação automaticamente (faz o commit se tudo rodar sem erros ou executa
o rollback se ocorrer alguma exceção).

💡 Principais Mudanças e Benefícios:
- commit e rollback Automáticos:
Ao usar with conexao:, você não precisa chamar conexao.commit() nem conexao.rollback()
manualmente. Se o bloco terminar com sucesso, a transação é efetuada no banco. Se qual
quer linha disparar um erro (como uma restrição de chave primária duplicada no INSERT),
o Python desfaz as alterações na hora.

- Fechamento da Conexão (finally):
Adicionamos o conexao.close() dentro do bloco finally para garantir que o recurso seja
liberado e o arquivo do banco SQLite desocupado, independente de ter dado erro ou não.

- Exceção Mais Específica:
Substituímos o except Exception genérico por except sqlite3.Error. Isso evita capturar
erros acidentais de sintaxe ou de sistema, focando apenas em falhas de banco de dados
(o que deixa o Ruff satisfeito e segue as boas práticas que vimos)

"""
# O 'with conexao' gerencia a transação (commit / rollback) automaticamente
try:
    with conexao:
        cursor = conexao.cursor()

        # cursor.execute("DELETE FROM clientes WHERE id = 8;")

        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            ("Teste 3", "teste3@gmail.com"),
        )
        cursor.execute(
            "INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)",
            (2, "Teste 4", "teste4@gmail.com"),
        )
        cursor.execute("DELETE FROM clientes WHERE id = 8")

except sqlite3.Error as exc:
    print(f"Ops! Um erro ocorreu no banco de dados: {exc}")

finally:
    conexao.close()
