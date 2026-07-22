import csv

class LeitorVendasAprovadas:
    """
    Iterador corporativo para processar arquivos de vendas pesados linha por linha.
    Economiza memória RAM processando apenas transações com status 'APROVADO'.
    """
    def __init__(self, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.arquivo = None
        self.leitor_csv = None

    def __iter__(self):
        # Abre o arquivo e inicializa o leitor de CSV no início do 'for'
        self.arquivo = open(self.caminho_arquivo, mode="r", encoding="utf-8")
        self.leitor_csv = csv.DictReader(self.arquivo)
        return self

    def __next__(self):
        # Percorre o arquivo linha a linha até encontrar uma venda APROVADA
        while True:
            try:
                linha = next(self.leitor_csv)
                
                # Regra de Negócio: Filtra apenas transações APROVADAS
                if linha.get("status") == "APROVADO":
                    return {
                        "id_transacao": linha["id"],
                        "cliente": linha["cliente"],
                        "valor": float(linha["valor"])
                    }
            except StopIteration:
                # Quando o arquivo terminar, fecha o arquivo com segurança e encerra o loop
                self.arquivo.close()
                raise StopIteration


# --- SIMULAÇÃO PRÁTICA NA EMPRESA ---

# Vamos criar um arquivo fictício 'vendas.csv' para testar a leitura
conteudo_csv = """id,cliente,valor,status
101,Empresa A,1500.00,APROVADO
102,Empresa B,320.50,CANCELADO
103,Empresa C,4500.00,PENDENTE
104,Empresa D,890.00,APROVADO"""

with open("vendas.csv", "w", encoding="utf-8") as f:
    f.write(conteudo_csv)


# --- EXECUTANDO O ITERADOR ---

print("--- Processando Vendas Aprovadas ---")

# O arquivo pode ter 1 milhão de linhas, mas a memória RAM ocupada será praticamente ZERO
# pois o Python só lê uma linha por vez da máquina!
for venda in LeitorVendasAprovadas("vendas.csv"):
    print(f"✅ Venda #{venda['id_transacao']} | Cliente: {venda['cliente']} | Valor: R$ {venda['valor']:.2f}")