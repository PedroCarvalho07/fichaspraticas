def do(carater, numero):
    if numero > 0:
        print(carater*numero)
        num = numero - 1
        do(carater, num)

numero = int(input( "Insira um numero :"))

do( '*', numero)