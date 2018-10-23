Lista1 = []

contador = 0
valores = 0
for item in range(1, 10 +1):
    item = int(input( " Insira os numeros que deseja: "))
    if item != -1:
        Lista1.append(item)
        contador = contador + 1
        valores = valores + item
        print(Lista1)
        if contador == 10:
            conta1 = valores / 10
            print ("conta1 : ", conta1)
    else:
        conta = valores / contador
        print (conta)
        break