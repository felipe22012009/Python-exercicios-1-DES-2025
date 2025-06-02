 dia_01 = int(input("dias para atividade 01"))
 dia_02 = int(input("dias para atividade 02"))
 dia_03 = int(input("dias para atividade 03"))

 if dia_01 < 0 or dia_02 < 0 or dia_03 < 0:
    print("erro números negativo")
else:
    soma = dias_01 + dias_02 + dias_03
    print(f"tempo total do projeto:{soma} dias")