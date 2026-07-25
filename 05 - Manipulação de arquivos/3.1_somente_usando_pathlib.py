from pathlib import Path

print('=' * 50)
ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)
print('=' * 50)

# 1. Cria a pasta (equivale ao os.mkdir)
# exist_ok=True evita erro caso a pasta já exista ao reexecutar
novo_dir = ROOT_PATH / "novo-diretorio"
novo_dir.mkdir(exist_ok=True)
print(ROOT_PATH)

# 2. Cria o "novo_arquivo.txt" DENTRO da pasta "novo-diretorio" (equivale ao open("w"))
# O método .touch() cria um arquivo vazio
arquivo_novo = novo_dir / "novo_arquivo.txt"
arquivo_novo.touch()

# 3. Exemplo: Cria um arquivo na raiz para demonstrar renomear/remover/mover
arquivo_raiz = ROOT_PATH / "arquivo_temp.txt"
arquivo_raiz.touch()

# 4. Renomeia o arquivo (equivale ao os.rename)
arquivo_alterado = ROOT_PATH / "alterado.txt"
arquivo_raiz.rename(arquivo_alterado)

# 5. Remove/Deleta o arquivo (equivale ao os.remove / os.unlink)
arquivo_alterado.unlink()

# 6. Mover / Mudar local de arquivo (equivale ao shutil.move)
# Vamos criar outro arquivo na raiz só para demonstrar a movimentação até o diretório:
arquivo_para_mover = ROOT_PATH / "mover_me.txt"
arquivo_para_mover.touch()

# Move o arquivo para dentro de 'novo-diretorio'
arquivo_para_mover.replace(novo_dir / "mover_me.txt")


