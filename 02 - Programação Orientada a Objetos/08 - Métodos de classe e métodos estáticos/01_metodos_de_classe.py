class Investimento:
    def __init__(self, nome, valor_inicial, taxa_anual):
        self.nome = nome
        self.valor_inicial = valor_inicial
        self.taxa_anual = taxa_anual  # Taxa em formato decimal (ex: 0.10)

    def __str__(self):
        return (f"Investimento: {self.nome} | "
                f"Valor: R$ {self.valor_inicial:.2f} | "
                f"Taxa: {self.taxa_anual * 100:.2f}% a.a.")

    # --- MÉTODOS DE CLASSE (CONSTRUTORES ALTERNATIVOS) ---

    @classmethod
    def criar_cdb_pos_fixado(cls, valor_inicial):
        """Atalho para criar um CDB padrão rendendo 10,75% ao ano"""
        nome_produto = "CDB Pós-Fixado 100% CDI"
        taxa_atual_cdi = 0.1075  
        
        # O 'cls' aqui é a própria classe 'Investimento'.
        # Retornar cls(...) é o mesmo que retornar Investimento(...)
        return cls(nome_produto, valor_inicial, taxa_atual_cdi)

    @classmethod
    def criar_tesouro_selic(cls, valor_inicial):
        """Atalho para criar um Tesouro Selic padrão rendendo 11,25% ao ano"""
        nome_produto = "Tesouro Direto Selic"
        taxa_selic_atual = 0.1125  
        
        return cls(nome_produto, valor_inicial, taxa_selic_atual)

# Criando investimentos usando os atalhos (métodos de classe)
carteira_marcus_cdb = Investimento.criar_cdb_pos_fixado(5000.00)
carteira_marcus_selic = Investimento.criar_tesouro_selic(10000.00)

# Criando um investimento personalizado pelo construtor comum
investimento_customizado = Investimento("Ações Petrobras", 2000.00, 0.15)

# Exibindo os resultados
print(carteira_marcus_cdb)
print(carteira_marcus_selic)
print(investimento_customizado)