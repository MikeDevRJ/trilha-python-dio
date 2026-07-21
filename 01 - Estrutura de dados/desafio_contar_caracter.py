def contar_caracteres(string):
    # TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    
    # TODO: Itere através de cada caractere na string string.
    for chave in string:
        # TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if chave in contador:
            contador[chave] += 1  # Se já existe, incrementa
        else:
            contador[chave] = 1   # Caso contrário, inicia com 1
            
    # O return deve ficar FORA do laço 'for'
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)