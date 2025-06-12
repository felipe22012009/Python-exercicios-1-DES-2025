alunos = ["alice", "bruno", "carla"]
dias = ["seg", "ter", "qua", "qui"]

# Inicializa a lista de reservas como uma lista de listas
reservas = [["ausente" for _ in dias] for _ in alunos]

print("Preencha com 'S' para presença e 'X' para ausência:")

for i, aluno in enumerate(alunos):
    print(f"\nAluno: {aluno}")
    for j, dia in enumerate(dias):
        entrada = input(f" {dia}: ")
        if entrada.upper() == 'S':
            reservas[i][j] = "presente"
        elif entrada.upper() == 'X':
            reservas[i][j] = "ausente"

print("\nTabela de reservas:")
print(f"{'Aluno':<10} {' '.join(f'{d:<10}' for d in dias)}")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '.join([f'{res:<10}' for res in reservas[i]])}")
