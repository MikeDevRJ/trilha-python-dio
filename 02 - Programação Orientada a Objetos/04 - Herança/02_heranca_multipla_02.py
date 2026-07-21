class Pessoa:
    # Recebe seus parâmetros e captura o resto em **kw para passar adiante
    def __init__(self, nome, sobrenome, **kw):
        super().__init__(**kw)  # Passa o que sobrou para a próxima classe (Paciente)
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Paciente:
    # Recebe seus parâmetros e captura o resto em **kw para passar adiante
    def __init__(self, nro_visita, exame, **kw):
        super().__init__(**kw)  # Passa o que sobrou para a próxima (object)
        self.nro_visita = nro_visita
        self.exame = exame

"""
    Um Mixin é um tipo especial de classe criada com um único objetivo:
    fornecer comportamentos (métodos) específicos e prontos para outras classes,
    sem que ela seja a classe pai principal delas.

 """

class MetodosMixin:
    def confirmar(self):
        return "Exame confirmado."


class Consulta(Pessoa, Paciente, MetodosMixin):
    def __init__(self, **kw):
        # Dispara a cadeia de inicialização cooperativa
        super().__init__(**kw)

        print(Consulta.mro())
        print(Consulta.__mro__)

consulta = Consulta(
    nome="Juliana", 
    sobrenome="Silva", 
    nro_visita="103", 
    exame="Antibiograma"
)

print(consulta)
print(consulta.confirmar())