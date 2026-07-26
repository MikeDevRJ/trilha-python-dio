def minha_funcao_teste(parametro1, parametro2):
    resultado = parametro1 + parametro2
    lista_exemplo = [1, 2, 3, 4, 5]

    # Usando a variável para que o aviso desapareça:
    print(f"Soma dos itens da lista: {sum(lista_exemplo)}")

    if resultado > 10:
        print("Resultado maior que 10: " + str(resultado))
    else:
        print("Resultado menor ou igual a 10")

    return resultado


class ContaBancaria:
    pass


x = minha_funcao_teste(5, 8)
y = [1, 2, 3, 4, 5]
z = {"chave": "valor", "outra_chave": 123}

frutas = [
    "pera",
    "maçã",
    "laranja",
    "uva",
    "melão",
    "morango",
    "abacate",
    "banana",
    "carambola",
    "pessego",
    "tamara",
    "melancia",
]
