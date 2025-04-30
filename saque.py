def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("❌ Limite diário de saques atingido.")
        return saldo, extrato, numero_saques

    valor = float(input("Informe o valor do saque: R$ "))

    if valor <= 0:
        print("❌ Valor inválido para saque.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > limite:
        print(f"❌ Saque excede o limite de R$ {limite:.2f} por operação.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")
    
    return saldo, extrato, numero_saques