# Crie a função 'soma_tupla' para receber uma tupla de números inteiros como argumento:
def multiplica(valor):
    valor = valor * 1
    return valor 

def soma_tupla(tupla):
    return sum(tupla)

if __name__ == "__main__":
    entrada = input()
    
    # Separa uma string em uma lista de elementos Ex.: "2 5 6 7 9"
    lista_elementos = entrada.split() # ['2', '5', '6', '7', '9']
        
    elementos = tuple(map(int, entrada.split()))
    
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
