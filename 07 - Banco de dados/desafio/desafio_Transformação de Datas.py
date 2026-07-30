"""

Você está desenvolvendo um sistema que integra com uma API de dados transacionais,
onde as datas são fornecidas no formato "DD-MM-YYYY". Sua tarefa é processar essa
lista de datas e transformá-las para o formato internacional "YYYY/MM/DD".

"""

# Recebe a entrada e armazena na variável "entrada"
# 01-01-2020;02-02-2021
entrada = input()


# Função responsável por receber as datas e transformar cada data para o formato "YYYY/MM/DD"
def transformar_datas(datas):
    # Divide a string de entrada nas datas individuais
    datas_lista = datas.split(";")

    datas_transformadas = []

    # TODO: Implemente a lógica necessária para formatar as datas
    for data in datas_lista:
        dia, mes, ano = data.split("-")
        nova_data = f"{ano}/{mes}/{dia}"
        datas_transformadas.append(nova_data)

    return datas_transformadas


# Imprime a lista de datas formatadas
print(transformar_datas(entrada))
