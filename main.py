"""
Validador de CPF

Programa que verifica se o CPF é válido ou não.
Versão: 1.2
"""
TAMANHO_LINHA = 78
TITULO = "Validador de CPF"
SEPARADORES = {".", "-", " "}


def limpar_cpf(cpf: str) -> str:
    """
    Função que limpa o CPF removendo suas pontuações.

    Args:
        cpf (str): CPF informado pelo usuário.

    Returns:
        str: CPF limpo somente com números.
    """
    cpf_limpo = cpf

    for separador in SEPARADORES:
        cpf_limpo = cpf_limpo.replace(separador, "")

    return cpf_limpo


def calcular_digito(base: str, peso_inicial: int) -> int:
    """
    Calcula um dígito verificador do CPF a partir de uma base numérica.

    Args:
        base (str): Sequência de dígitos usada no cálculo (9 ou 10 dígitos).
        peso_inicial (int): Peso inicial do cálculo (10 ou 11).

    Returns:
        int: Dígito verificador calculado (0 a 9).
    """
    soma = 0
    peso = peso_inicial

    for digito in base:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def validar_cpf(cpf_limpo: str) -> bool:
    """
    Valida um CPF limpo (apenas dígitos), incluindo os dígitos verificadores.

    Args:
        cpf_limpo (str): CPF já limpo, contendo apenas números.

    Returns:
        bool: True se o CPF for válido, caso contrário False.
    """
    if (
        len(cpf_limpo) != 11
        or not cpf_limpo.isdigit()
        or len(set(cpf_limpo)) == 1
    ):
        return False

    base9 = cpf_limpo[:9]
    base10 = cpf_limpo[:10]
    digito10 = int(cpf_limpo[9])
    digito11 = int(cpf_limpo[10])

    digito10_calculado = calcular_digito(base9, 10)
    digito11_calculado = calcular_digito(base10, 11)

    return digito10_calculado == digito10 and digito11_calculado == digito11


def caracteres_permitidos(cpf: str) -> bool:
    """
    Verifica se os caracteres do CPF são permitidos.

    Args:
        cpf (str): CPF informado pelo usuário.

    Returns:
        bool: True se for permitido, False caso contrário.
    """
    for caractere in cpf:
        if caractere.isdigit() or caractere in SEPARADORES:
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
        print("=" * TAMANHO_LINHA)
        return

    cpf_limpo = limpar_cpf(cpf)

    if not validar_cpf(cpf_limpo):
        print("Erro: CPF inválido.")
        print("=" * TAMANHO_LINHA)
        return

    print("CPF válido:", cpf_limpo)
    print("=" * TAMANHO_LINHA)


# Proteção padrão:
if __name__ == "__main__":
    main()
