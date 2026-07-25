# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!
"""
arquivo = open(
    "C:/Users/mlmag/OneDrive/Área de Trabalho/Tutoriais Python/DIO/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt",
    "r",
)
print(arquivo.read())
arquivo.close()

print('\n')

"""
print('\n========================')

arquivo = open(
    "C:/Users/mlmag/OneDrive/Área de Trabalho/Tutoriais Python/DIO/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

print('\n========================')

arquivo = open(
    "C:/Users/mlmag/OneDrive/Área de Trabalho/Tutoriais Python/DIO/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()

print('\n========================')

arquivo = open(
    "C:/Users/mlmag/OneDrive/Área de Trabalho/Tutoriais Python/DIO/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
