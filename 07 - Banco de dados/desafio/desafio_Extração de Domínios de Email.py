"""

Os domínios de email são essenciais para categorizar e identificar a origem dos contatos,
facilitando a segmentação e análise dos dados. Sabendo disso, sua função será receber uma
string contendo múltiplos emails separados por ";" e retornar uma lista contendo apenas os
domínios de cada um desses emails.

"""

# Recebe a entrada e armazena na variável "entrada"
# ana@example.com;bob@test.com
entrada = input()


# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(";")

    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = [email.split("@")[1] for email in lista_emails]

    return dominios


# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))
