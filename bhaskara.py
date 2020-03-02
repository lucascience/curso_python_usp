import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    lista = [raiz1, raiz2]
    lista.sort()
    if delta == 0:
        print("a raiz desta equação é", raiz1)
    else:  
        print("as raízes da equação são", ' e '.join(map(str, lista)))
