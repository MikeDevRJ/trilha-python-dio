"""
A função map em Python é uma função built-in que permite aplicar uma função a todos
os itens de uma sequência (como listas ou tuplas) e retornar uma nova sequência com
os resultados. Em outras palavras, ela “mapeia” cada valor da sequência original para
um novo valor, de acordo com a função fornecida.

A sintaxe básica da função map é a seguinte:

map(funcao, sequencia)


Exemplo 1: Convertendo Temperaturas
Suponha que você tenha uma lista de temperaturas em Celsius e queira convertê-la
para Fahrenheit. Você pode fazer isso facilmente com a função map()

"""

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_celsius = [0, 22.5, 40, 100]
temperaturas_fahrenheit = list(map(celsius_para_fahrenheit, temperaturas_celsius))

print(temperaturas_fahrenheit) # Saída: [32.0, 72.5, 104.0, 212.0]

#Exemplo 2: Usando Funções Lambda
#Você também pode usar funções lambda (funções anônimas) com map para tornar o código mais conciso.

temperaturas_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas_celsius))

print(temperaturas_fahrenheit) # Saída: [32.0, 72.5, 104.0, 212.0]