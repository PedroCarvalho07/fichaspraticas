num_alunos = 10 
max = 20
min = 0

def lerinteiro(min,max):
    num = min - 1
    while num < min or num > max :
        num = int(input(" Introduza o numero inteiro : "))
        return num

def lernotas():
    soma = 0
    for item in range(0,10):
        soma += lerinteiro(0,20)
    media = soma / 10
    print(" A média é :", media)
    return 

lernotas()

