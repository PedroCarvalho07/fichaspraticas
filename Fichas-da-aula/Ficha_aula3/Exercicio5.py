resultado = 0
contar = 0
soma = 0
while True: 
    num=int(input('Introduza um valor: '))
    if num == -1 :
        break

    contar = contar + 1
    soma = soma + num
    
    if contar != 0 :
        resultado = soma / contar
print(resultado)