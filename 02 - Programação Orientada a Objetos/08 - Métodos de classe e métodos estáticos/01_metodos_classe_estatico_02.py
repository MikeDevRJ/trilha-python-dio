class Data:
    def __init__(self, dia=0, mes=0, ano=0):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Exibição bonita do objeto quando dermos 'print'
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"
    
        """
        Para que serve ?
         É muito usado como um construtor alternativo (padrão Factory),
         permitindo criar instâncias da classe a partir de formatos diferentes
         (como um texto vindo de um banco de dados ou de uma API).

        """

    @classmethod
    def de_string(cls, data_em_string):
        print(f"-> Dentro do @classmethod. Parâmetro 'cls' aponta para: {cls}")
        dia, mes, ano = map(int, data_em_string.split('-'))
        return cls(dia, mes, ano)
    
        """
        Para que serve ?
            Serve para agrupar funções de validação, cálculos auxiliares ou utilitários
            que fazem sentido lógico estar "dentro" do contexto daquela classe, mas que
            não precisam ler ou modificar nenhuma informação interna dela.

        """


    @staticmethod
    def data_e_valida(data_em_string):
        dia, mes, ano = map(int, data_em_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 3999


# --- CHAMADAS E TESTES ---

# 1. Chamando o Método Estático (@staticmethod)
# Ele funciona como uma função utilitária. Não precisa gerar um objeto para ser usado.
string_teste = "16-07-2026"
e_valida = Data.data_e_valida(string_teste)
print(f"A data {string_teste} é válida? {e_valida}\n")

# 2. Chamando o Método de Classe (@classmethod)
# Ele funciona como um construtor alternativo (fábrica de objetos).
nova_data = Data.de_string(string_teste)
print(f"Objeto Data criado com sucesso: {nova_data}")