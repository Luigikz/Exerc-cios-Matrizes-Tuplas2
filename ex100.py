print("Bem-vindo ao programa")
print()

LINHAS = 3
COLUNAS = 3

matriz = [[0] * COLUNAS for i in range(LINHAS)]
identidade = True

for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j] = int(input(f"Informe o valor da posição [{i}][{j}]: "))

        if i == j and matriz[i][j] != 1:
            identidade = False
        elif i != j and matriz[i][j] != 0:
            identidade = False

print()
print("Matriz:")

for i in range(LINHAS):
    print(matriz[i])

print()

if identidade:
    print("A matriz é identidade")
else:
    print("A matriz não é identidade")