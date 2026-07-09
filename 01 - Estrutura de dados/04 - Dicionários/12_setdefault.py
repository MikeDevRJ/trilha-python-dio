contato = {"nome": "Guilherme", "telefone": "3333-2221", 'DDD':21}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

telefone_DDD = contato["DDD"]
print(telefone_DDD)

if telefone_DDD == 21:
    contato.setdefault("UF", "RJ")

print(contato)

