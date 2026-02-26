"""
Validador de CPF

Programa que verifica se o CPF é válido ou não.
Versão: 1.0
"""
TAMANHO_LINHA = 78
TITULO = "Validador de CPF"


def validar_cpf(cpf: str) -> bool:
    """
    Valida se o CPF possui exatamente 11 dígitos numéricos.

    Args:
        cpf (str): CPF informado pelo usuário.

    Returns:
        bool: True se válido no formato, False caso contrário.
    """

    return len(cpf) == 11 and cpf.isdigit()


def main():
    """
    Função principal que executa o fluxo do programa.
    """

    print("=" * TAMANHO_LINHA)
    print(TITULO.center(TAMANHO_LINHA))
    print("=" * TAMANHO_LINHA)

    cpf = input("Digite o CPF: ")
    cpf_valido = validar_cpf(cpf)

    if cpf_valido:
        print("O CPF digitado é válido.")
    else:
        print("O CPF digitado não é válido.")

    print("=" * TAMANHO_LINHA)


# Proteção padrão:
if __name__ == "__main__":
    main()
