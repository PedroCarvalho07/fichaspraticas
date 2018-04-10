num_alunos = 10 
max = 20
min = 0

def lerinteiro(min,max) :
    soma = 0
    num = min -1
    while num < min or num > max :
        for i in range(0, 10):
            num = int(input(" Introduza um numero inteiro : "))
            soma += num
        media = soma / 10
        print(" A média é : ",media)
      

lerinteiro(0,20)

