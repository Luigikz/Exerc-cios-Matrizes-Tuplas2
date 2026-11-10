print("Bem-vindo ao programa!")
print()

matriz = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        matriz[i][j] = float(input(f"Informe o valor da posição [{i}][{j}]: "))

a = matriz[0][0]
b = matriz[0][1]
c = matriz[1][0]
d = matriz[1][1]

determinante = (a * d) - (b * c)

print()
print("Matriz:")
for i in range(2):
    print(matriz[i])

print()
print(f"Determinante = {determinante}")
