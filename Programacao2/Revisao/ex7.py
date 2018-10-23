NUN_ALUNOS = 10
max = 20
min = 0

def lerinteiro(min, max):
    num = min - 1
    while num < min or num > max :
        num = int(input(" Introduza o numero inteiro : "))
        return num

def lernotas():
    soma = 0
    for _ in range(0,NUN_ALUNOS):
        soma += lerinteiro(0, 20)
    media = soma / NUN_ALUNOS
    print(" A média é :", media)
    return 

lernotas()

