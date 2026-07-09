def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

modelo  = "Sandero"
ano     = 2015
placa   = "KZI-1234"
marca   = "Renault"
motor   = "1.0"
combustivel = "Flex"

criar_carro(modelo, ano, placa, marca, motor, combustivel)
