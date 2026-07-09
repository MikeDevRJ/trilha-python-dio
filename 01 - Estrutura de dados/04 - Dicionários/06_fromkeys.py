resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado1 = contatos.fromkeys(["nome", "telefone", "CEP"])
print(resultado1)