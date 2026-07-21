class Carro:
    def __init__(self, marcha_atual):
        self.marcha = marcha_atual  # Guarda a marcha atual do objeto

    def trocar_marcha(self, nro_marcha):
        print(f"Trocando marcha para marcha {nro_marcha}")

        def _trocar_marcha():
            # O Python já enxerga o 'self' e o 'nro_marcha' aqui dentro nativamente
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
                self.marcha = nro_marcha  # Atualiza a marcha do carro
            else:
                print("Não foi possível trocar de marcha...")
        
        _trocar_marcha()
   
# 1. Criamos um carro que começa na marcha 2
meu_carro = Carro(marcha_atual=2)

# 2. Teste 1: Tentar ir para uma marcha MAIOR (3 > 2) -> Deve funcionar
meu_carro.trocar_marcha(3) 

# 3. Teste 2: Tentar ir para uma marcha MENOR ou IGUAL (1 > 3) -> Deve falhar
meu_carro.trocar_marcha(1)   
   