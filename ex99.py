print("Bem-vindo ao programa!")
print()

pessoas = []

for i in range(10):
    nome = input(f"Informe o nome da pessoa {i + 1}: ")
    idade = int(input(f"Informe a idade de {nome}: "))

    pessoa = (nome, idade)
    pessoas.append(pessoa)

print()
print("Pessoas menores de 18 anos:")

for pessoa in pessoas:
    if pessoa[1] < 18:
        print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]}")

print()
print("Pessoas com 18 anos ou mais:")

for pessoa in pessoas:
    if pessoa[1] >= 18:
        print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]}")