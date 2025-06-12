import random

input("Presione o enter para lançar o dado")

resultado = random.randint(1,6)

print(f"O dado rolou : {resultado}");

if resultado == 6 :
    print("Parabéns, você conseguiu")