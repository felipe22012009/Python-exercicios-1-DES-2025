distancia = int(input("Digite a distância: "))

if distancia <= 50:
    frete = 15.00
elif distancia <= 150:
    frete = 15.00
else:
    frete = 25.00

print(f"O custo do frete para {distancia} km é R$ {frete:.2f}")
