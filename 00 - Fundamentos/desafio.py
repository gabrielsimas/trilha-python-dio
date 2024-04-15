from typing import Tuple


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


def sistema_bancario_controller() -> None:
    saldo = 0
    LIMITE_SAQUE_VALOR: int = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES: int = 3

    while True:

        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = gerenciar_deposito(saldo, extrato)

        elif opcao == "s":
            saldo, numero_saques, extrato = gerenciar_saque(
                saldo, LIMITE_SAQUE_VALOR, LIMITE_SAQUES, numero_saques, extrato
            )

        elif opcao == "e":
            imprimir_extrato(saldo, extrato)

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


def gerenciar_deposito(saldo: float, extrato: str) -> Tuple[float, str]:
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"R$ {valor:.2f} [C]\n"

    else:
        print("A Operação não pôde ser concluída! O valor de depósito é inválido.")

    return saldo, extrato


def gerenciar_saque(
    saldo: float, LIMITE_SAQUE_VALOR, LIMITE_SAQUES, numero_saques, extrato
) -> Tuple[float, int, str]:
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > LIMITE_SAQUE_VALOR

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"R$ -{valor:.2f} [D]\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, numero_saques, extrato


def imprimir_extrato(saldo: float, extrato: str) -> None:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


sistema_bancario_controller()
