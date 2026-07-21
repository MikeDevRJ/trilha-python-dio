class Investimento:
    def __init__(self, nome, valor_inicial):
        self.nome = nome
        self.valor_inicial = valor_inicial

    @staticmethod
    def calcular_valor_futuro(pv, i, n):
        """
        Calcula o Valor Futuro (Future Value)
        pv: Present Value (Valor Presente / Capital Inicial)
        i: Interest rate (Taxa de juros decimal, ex: 0.10 para 10%)
        n: Period (Número de períodos / prazo)
        """
        # Aplicação direta da fórmula matemática: PV * (1 + i)^n
        return pv * ((1 + i) ** n)


# --- COMO TESTAR ---

# Repare que NÃO precisamos criar um objeto "Investimento" para usar o cálculo.
# Chamamos a função diretamente através da classe:

capital_inicial = 1000.00  # PV
taxa_juros = 0.10          # i (10% ao ano)
periodo = 5                # n (5 anos)

valor_final = Investimento.calcular_valor_futuro(capital_inicial, taxa_juros, periodo)

print(f"O Valor Futuro após {periodo} anos será de: R$ {valor_final:.2f}")
# Saída esperada: O Valor Futuro após 5 anos será de: R$ 1610.51