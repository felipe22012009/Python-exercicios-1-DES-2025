 
dia_01 = int(input("Dias para atividade 01: "))
dia_02 = int(input("Dias para atividade 02: "))
dia_03 = int(input("Dias para atividade 03: "))

if dia_01 < 0 or dia_02 < 0 or dia_03 < 0:
    print("Erro: números negativos não são permitidos.")
else:
    soma = dia_01 + dia_02 + dia_03
    print(f"Tempo total do projeto: {soma} dias")

