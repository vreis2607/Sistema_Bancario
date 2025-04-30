def depositar(saldo, extrato):
    valor_str = input("Informe o valor do depósito: R$ ").strip()
    try:
        valor = float(valor_str.replace('.', '').replace(',', '.'))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("✅ Depósito realizado com sucesso.")
        else:
            print("❌ Valor inválido para depósito.")
    except ValueError:
        print("❌ Formato inválido. Use números como: 1500.57 ou 1.500,57")

    return saldo, extrato