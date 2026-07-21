import functools

"""
    Aqui está um exemplo real focado em Autenticação e Controle de Acesso (Autorização).

    Esse é exatamente o padrão utilizado por frameworks web profissionais (como Flask, 
    FastAPI e Django) para proteger rotas e funções de sistema, garantindo que apenas 
    usuários com as permissões corretas executem determinada ação.

"""

# Simulação do usuário logado na sessão do sistema
usuario_logado = {
    "nome": "Marcus Magina",
    "funcao": "Desenvolvedor",  # Opções: "Admin", "Gerente", "Desenvolvedor"
    "autenticado": True
}


def requer_permissao(funcao_permitida):
    """
    Decorador que verifica se o usuário logado possui 
    a permissão necessária para executar a ação.
    """
    def decorador(funcao_original):
        @functools.wraps(funcao_original)
        def envelope(*args, **kwargs):
            # 1. Verifica se o usuário está autenticado
            if not usuario_logado.get("autenticado"):
                print("❌ [ACESSO NEGADO] Usuário não está autenticado no sistema.")
                return None

            # 2. Verifica se a função do usuário é compatível com a permissão exigida
            funcao_usuario = usuario_logado.get("funcao")
            if funcao_usuario != funcao_permitida and funcao_usuario != "Admin":
                print(
                    f"⛔ [ACESSO NEGADO] O usuário '{usuario_logado['nome']}' "
                    f"({funcao_usuario}) não tem permissão de '{funcao_permitida}'."
                )
                return None

            # 3. Se passou nas validações, executa a função original
            print(f"✅ [ACESSO AUTORIZADO] Executando '{funcao_original.__name__}'...")
            return funcao_original(*args, **kwargs)

        return envelope
    return decorador


# --- APLICAÇÃO PRÁTICA NA REGRA DE NEGÓCIO ---

@requer_permissao(funcao_permitida="Admin")
def deletar_banco_de_dados():
    print("🔥 [OPERAÇÃO CRÍTICA] Banco de dados resetado com sucesso.")

@requer_permissao(funcao_permitida="Desenvolvedor")
def atualizar_codigo_servidor():
    print("🚀 [DEPLOY] Código atualizado no ambiente de homologação.")


# --- EXECUTANDO O SISTEMA ---

print("--- Tentativa 1: Atualizar código no servidor ---")
atualizar_codigo_servidor()

print("\n--- Tentativa 2: Deletar banco de dados ---")
deletar_banco_de_dados()