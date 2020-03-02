import math

x1 = float(input('Digite a coordenada X do ponto A: '))
y1 = float(input('Digite a coordenada Y do ponto A: '))

x2 = float(input('Digite a coordenada X do ponto B: '))
y2 = float(input('Digite a coordenada Y do ponto B: '))

distAB = math.sqrt( ((x1 - x2) ** 2) + ((y1 - y2) ** 2) )

if distAB >= 10:
    print("longe")
else:
    print("perto")
