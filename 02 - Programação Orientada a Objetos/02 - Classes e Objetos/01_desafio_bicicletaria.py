class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        print(self.__dict__.items())
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    #def __str__(self):
    #    return f"O nome da classe é {self.__class__.__name__}"

obj = Bicicleta("vermelha", "caloi", 2022, 600)
obj.buzinar()
obj.correr()
obj.parar()
print(f'Imprimindo a instancia da classe Bicicleta => {obj}')
print(obj.cor, obj.modelo, obj.ano, obj.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
