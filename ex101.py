print("Bem-vindo ao programa!")
print()

LINHAS = 3
COLUNAS = 3

matriz = [[0] * COLUNAS for i in range(LINHAS)]

for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j] = int(input(f"Informe o valor da posição [{i}][{j}]: "))

a = matriz[0][0]
b = matriz[0][1]
c = matriz[0][2]
d = matriz[1][0]
e = matriz[1][1]
f = matriz[1][2]
g = matriz[2][0]
h = matriz[2][1]
i = matriz[2][2]

determinante = (a * e * i) + (b * f * g) + (c * d * h) - (c * e * g) - (b * d * i) - (a * f * h)

print()
print("Matriz:")

for i in range(LINHAS):
    print(matriz[i])

print()
print(f"Determinante = {determinante}")