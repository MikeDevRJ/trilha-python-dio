def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 5, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 5, subtrair)  # O resultado da operação 10 - 5 = 5

operacao = somar
print(operacao(1,24))

