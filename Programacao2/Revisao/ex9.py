def num(numero):
    for i in range(1, numero +1):
        if numero % i == 0:
            print(i)
    

numero = int(input(" Escolha um numero que deseja: "))
num(numero)