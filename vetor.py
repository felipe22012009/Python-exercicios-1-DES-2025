import random

frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga"]
print("Lista de frutas:")
for i in range(len(frutas)):
    print(f"{i + 1} - {frutas[i]}")

posição_sorteada = random.randint(1, 5)
palpite = input("Qual fruta você acha que está na posição? ")
fruta_certa = frutas[posição_sorteada - 1]

if palpite.capitalize() == fruta_certa:
    print("Parabéns! Você acertou!")
    print(f"A fruta na posição {posição_sorteada} era realmente {fruta_certa}.")
else:
    print("Que pena, você errou.")
    print(f"A fruta na posição {posição_sorteada} era {fruta_certa}.")
