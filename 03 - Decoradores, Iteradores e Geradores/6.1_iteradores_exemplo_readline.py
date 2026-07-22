class FileIterator:
    def __init__(self, filename):
        self.file = open(filename, mode="r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        
        # Se line não for vazia (ainda há conteúdo para ler)
        if line != "":
            return line
        else:
            # Chegou ao fim do arquivo: fecha o ponteiro e encerra a iteração
            self.file.close()
            raise StopIteration


# --- 1. CRIANDO O ARQUIVO FICTÍCIO ---
nome_arquivo = "large_file.txt"

conteudo_ficticio = """Primeira linha do arquivo de logs.
Segunda linha: Processamento em andamento...
Terceira linha: Operação realizada com sucesso!
Quarta linha: Fim dos registros."""

with open(nome_arquivo, mode="w", encoding="utf-8") as f:
    f.write(conteudo_ficticio)


# --- 2. USO DO FileIterator (CHAMADA) ---
print("--- Lendo o arquivo linha por linha ---")

for line in FileIterator(nome_arquivo):
    # O .strip() remove a quebra de linha extra (\n) ao imprimir no console
    print(line.strip())''