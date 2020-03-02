num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um novo número inteiro: "))
num3 = int(input("Digite mais um número inteiro: "))

lista = [num1, num2, num3]

if sorted(lista) == lista:
    print("crescente")
else:
    print("não está em ordem crescente")
