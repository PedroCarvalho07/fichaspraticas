def lerinteiro(min,max) :
    num = min -1
    while num < min or num > max :
        num = int(input(" Introduza um numero inteiro :"))
    return num
def valor() :
    num = lerinteiro(0,100)
    print('*' * num)

valor()