"""
CLASSE ABSTRATA:

No dia a dia do desenvolvimento de software, o uso mais comum, prático e poderoso de um método abstrato
é a criação de Gateways de Integração (como sistemas de pagamento, envio de notificações ou conexões com
bancos de dados).

Imagine que você está desenvolvendo um e-commerce. Hoje você usa o Stripe para processar pagamentos, mas 
amanhã a empresa pode decidir mudar para o PayPal ou PagSeguro. Se você escrever o código do seu e-commerce
acoplado diretamente às regras de um único provedor, mudar de sistema no futuro será um pesadelo.


A solução é criar uma "classe molde" abstrata que dita as regras de como qualquer meio de pagamento
deve se comportar no seu sistema.

O Conceito Visual de Abstração:
O método abstrato funciona como um contrato obrigatório. A classe abstrata define o que deve ser feito,
mas deixa para as classes filhas a responsabilidade de decidir como fazer.

Exemplo Prático: Sistema de Pagamentos do E-commerce
No Python, criamos classes abstratas utilizando o módulo nativo abc (Abstract Base Classes)
e o decorador @abstractmethod.

"""
from abc import ABC, abstractmethod

"""
A obrigatoriedade do contrato.
Ao colocar o decorador @abstractmethod em cima do método processar_pagamento,
você criou uma regra rígida de arquitetura.
Se outro desenvolvedor da sua equipe criar uma classe GatewayPagSeguro herdando
de ProcessadorPagamento, mas esquecer de programar o método processar_pagamento
lá dentro, o Python não vai deixar o código dele rodar até que ele escreva a função.

"""


# 1. A CLASSE ABSTRATA (O contrato)
class ProcessadorPagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self, valor: float) -> bool:
        
        """
        Qualquer classe de pagamento que herdar de ProcessadorPagamento
        é OBRIGADA a implementar este método com essa assinatura exata.
        """
        pass


# 2. IMPLEMENTAÇÃO REAL 1 (Gateway Stripe)
class GatewayStripe(ProcessadorPagamento):
    def processar_pagamento(self, valor: float) -> bool:
        print(f"Conectando à API do Stripe...")
        print(f"Cobrando R$ {valor:.2f} via Cartão de Crédito internacional.")
        # Simula uma resposta de sucesso da API externa
        return True


# 3. IMPLEMENTAÇÃO REAL 2 (Gateway PayPal)
class GatewayPayPal(ProcessadorPagamento):
    def processar_pagamento(self, valor: float) -> bool:
        print(f"Redirecionando para o fluxo seguro do PayPal...")
        print(f"Cobrando R$ {valor:.2f} do saldo da conta digital.")
        return True
    
# Esta função do carrinho de compras serve para QUALQUER meio de pagamento atual ou futuro!
def finalizar_compra(carrinho_valor: float, meio_pagamento: ProcessadorPagamento):
    print("Iniciando fechamento do pedido...")
    
    # Nós confiamos que 'processar_pagamento' existe por causa do contrato abstrato
    sucesso = meio_pagamento.processar_pagamento(carrinho_valor)
    
    if sucesso:
        print("Pedido finalizado com sucesso ! Enviando para separação.\n")
    else:
        print("Falha no pagamento. Compra retida.\n")


# --- TESTANDO NO DIA A DIA ---

# Hoje o cliente escolheu pagar com Stripe:
pagamento_stripe = GatewayStripe()
finalizar_compra(150.00, pagamento_stripe)

# Amanhã o cliente escolheu pagar com PayPal:
pagamento_paypal = GatewayPayPal()
finalizar_compra(89.90, pagamento_paypal)    
    
"""
A classe ProcessadorPagamento herda de ABC. Isso diz ao interpretador do Python: "Esta classe é
apenas conceitual, não permita que ninguém crie um objeto diretamente dela."
Se você tentar rodar o código abaixo, o Python vai travar e disparar um erro de
compilação imediatamente:    

"""    
# ISSO VAI GERAR ERRO: TypeError: Can't instantiate abstract class ProcessadorPagamento without an implementation for abstract method 'processar_pagamento'
# meu_pagamento = ProcessadorPagamento()    