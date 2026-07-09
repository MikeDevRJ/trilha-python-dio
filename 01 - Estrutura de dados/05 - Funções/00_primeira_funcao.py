def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_4(valor):
    print(f"Seja bem vindo {valor}!")   


exibir_mensagem()

exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

nome = 'Marcus'
exibir_mensagem_4(nome)
