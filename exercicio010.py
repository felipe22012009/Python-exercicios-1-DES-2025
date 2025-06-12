salario_mes = float(input("Digite o salário do mês de Renata: "))
parcela_maxima = salario_mes * 0.35

if salario_mes > 3000:
    print("Renata tem salário superior a R$ 3.000,00")
    print(f"A parcela máxima que ela pode ter é: R$ {parcela_maxima:.2f}")
else:
    print("O salário do mês de Renata é inferior ou igual a R$ 3.000,00.")
    print("Ela não pode ter parcela máxima maior que 35% do salário.")


