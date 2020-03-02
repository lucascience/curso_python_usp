n = input("Digite um número inteiro: ")
caracteres = len(n)
numadj = False
aux1=0
aux2=0

while not numadj:
  aux1 = int(n) // (10 ** (caracteres - 1))

  n = int(n) % (10 ** (caracteres - 1))
  
  caracteres = caracteres - 1
  
  aux2 = n // (10**(caracteres - 1))

  if aux1 == aux2 and caracteres > 0:
    numadj=True  
    print("sim")
  elif caracteres == 0:
    numadj=True
    print("não")
