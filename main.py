"""
Validador de CPF

Programa que verifica se o CPF é válido ou não.
Versão: 1.1
"""
TAMANHO_LINHA = 78
TITULO = "Validador de CPF"


def limpar_cpf(cpf: str) -> str:
    """
    Função que limpa o CPF removendo suas pontuações.

    Args:
        cpf (str): CPF informado pelo usuário.
    Returns:
        str: CPF limpo somente com números.
    """

    cpf_limpo = cpf.replace(".", "").replace("-", "").replace(" ", "")

    return cpf_limpo


def validar_cpf(cpf_limpo: str) -> bool:
    """
    Valida se o CPF possui exatamente 11 dígitos numéricos.

    Args:
        cpf_limpo (str): CPF já limpo.

    Returns:
        bool: True se válido no formato, False caso contrário.
    """

    return len(cpf_limpo) == 11 and cpf_limpo.isdigit()


def caracteres_permitidos(cpf: str) -> bool:
    """
    Verifica se os caracteres do CPF são permitidos.

    Args:
        cpf (str): CPF informado pelo usuário

    Returns:
        bool: True se for permitido, False caso contrário.
    """

    for caractere in cpf:
        if caractere.isdigit() or caractere == '.' or caractere == '-' or caractere == ' ':
            continue
        else:
            return False

    return True


def main():
    """
    Função principal que executa o fluxo do programa.
    """

    print("=" * TAMANHO_LINHA)
    print(TITULO.center(TAMANHO_LINHA))
    print("=" * TAMANHO_LINHA)

    cpf = input("Digite o CPF: ")

    if not caracteres_permitidos(cpf):
        print("Erro: CPF contém caracteres inválidos.")
    else:
        cpf_limpo = limpar_cpf(cpf)
        if not validar_cpf(cpf_limpo):
            print("Erro: CPF deve ter exatamente 11 dígitos.")
        else:
            print("CPF válido:", cpf_limpo)

    print("=" * TAMANHO_LINHA)


# Proteção padrão:
if __name__ == "__main__":
    main()
