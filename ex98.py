print("Bem-vindo ao programa!")
print()

LINHAS = 4
COLUNAS = 3

matriz1 = [[0] * COLUNAS for i in range(LINHAS)]
matriz2 = [[0] * COLUNAS for i in range(LINHAS)]
soma = [[0] * COLUNAS for i in range(LINHAS)]

print("Digite os valores da primeira matriz:")
for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz1[i][j] = int(input(f"Matriz1[{i}][{j}]: "))

print()
print("Digite os valores da segunda matriz:")
for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz2[i][j] = int(input(f"Matriz2[{i}][{j}]: "))

for i in range(LINHAS):
    for j in range(COLUNAS):
        soma[i][j] = matriz1[i][j] + matriz2[i][j]

print()
print("Matriz Soma:")

for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f"{soma[i][j]:4}", end="")
    print()