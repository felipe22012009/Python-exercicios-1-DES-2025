aluno = ["alice", "bruno", "carla",]
dias = ["seg", "ter", "qua", "qui",]

reserva = [{"ausente" for _ in dias} for _ in alunos"]

print("preencha com 'S' para presença e 'X' para ausência:")

for i, aluno in enumerate(aluno) :
    print(f"\nAluno: {aluno}")
    for j, dia in enumerate(dias):
        entrada = input(f" {dia}: ")
        if entrada.upper() == 'S':
            reservas[i][j] = "presentes"

print("\nTabela de reservas:")
print(f"{'Aluno'} {' '.join(f'{d:<10}' for d in dias)}")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '.join([f'{res:<10}' for res in reservas[i]])}")