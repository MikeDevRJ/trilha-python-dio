class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
         # Inspecionando o valor de self no momento em que o 'for' começa
        print(f"--> [__iter__ chamado] Endereço da instância na memória (self): {self}")
        print(f"--> [__iter__ chamado] Estado inicial de self: numeros={self.numeros}, contador={self.contador}")
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(f"Item recebido no loop: {i}")
