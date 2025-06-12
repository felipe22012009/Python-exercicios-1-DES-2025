media1 = float(input("Digite a primeira média: "))
media2 = float(input("Digite a segunda média: "))
media3 = float(input("Digite a terceira média: "))

soma = media1 + media2 + media3
media = soma / 3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")
