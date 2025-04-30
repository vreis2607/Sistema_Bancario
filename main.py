from deposito import depositar
from saque import sacar
from extrato import exibir_extrato
from utils import LIMITE_SAQUES, LIMITE_SAQUE_DIARIO

def main():
    saldo = 0.0
    extrato = ""
    numero_saques = 0

    while True:
        print("""
        ================= MENU =================
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
        ========================================
        """)
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                saldo, extrato = depositar(saldo, extrato)

            case "2":
                saldo, extrato, numero_saques = sacar(
                    saldo, extrato, numero_saques, LIMITE_SAQUE_DIARIO, LIMITE_SAQUES
                )

            case "3":
                exibir_extrato(saldo, extrato)

            case "0":
                print("👋 Obrigado por usar o sistema bancário. Até mais!")
                break

            case _:
                print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()