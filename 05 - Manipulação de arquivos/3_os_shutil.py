import os
import shutil
from pathlib import Path

print('=' * 50)
#print(__file__)
#ROOT_PATH = Path(__file__)
ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)
print('=' * 50)

os.mkdir(ROOT_PATH / "novo-diretorio")
print(ROOT_PATH)

arquivo = open(ROOT_PATH / "novo_arquivo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "novo-diretorio" / "novo_arquivo.txt")


