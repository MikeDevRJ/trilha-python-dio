import functools
import time

def audit_e_performance(funcao):
    """
    Decorador corporativo para medir o tempo de execução 
    e registrar logs de auditoria das operações.
    """
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        nome_funcao = funcao.__name__
        print(f"[LOG INÍCIO] Executando a operação: {nome_funcao}...")
        
        inicio = time.time()  # Marca o tempo inicial
        
        # Executa a função original de negócio e guarda o retorno
        resultado = funcao(*args, **kwargs)
        
        fim = time.time()  # Marca o tempo final
        duracao = fim - inicio
        
        print(f"[LOG SUCESSO] Operação '{nome_funcao}' concluída em {duracao:.4f} segundos.")
        print("-" * 50)
        
        return resultado  # Retorna o resultado da função original

    return envelope


# --- APLICAÇÃO PRÁTICA NA REGRA DE NEGÓCIO ---

@audit_e_performance
def processar_pagamento(id_transacao, valor):
    # Simula um processamento bancário
    time.sleep(1.2) 
    print(f"💰 Pagamento da transação #{id_transacao} no valor de R$ {valor:.2f} aprovado.")
    return True

@audit_e_performance
def gerar_relatorio_mensal(mes, ano):
    # Simula a geração de um relatório pesado
    time.sleep(0.8)
    print(f"📊 Relatório financeiro de {mes}/{ano} gerado com sucesso.")
    return "relatorio_final.pdf"


# --- EXECUTANDO O SISTEMA ---

pagamento_ok = processar_pagamento(id_transacao=98231, valor=450.00)
pdf = gerar_relatorio_mensal(mes="Julho", ano=2026)

# O __name__ continua intacto graças ao @functools.wraps
print(f"Nome da função mantido: {processar_pagamento.__name__}")