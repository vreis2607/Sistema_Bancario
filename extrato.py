def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================\n")