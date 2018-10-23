def do(carater, numero):
    if numero > 0:
        print(carater*numero)
        num = numero - 1
        do(carater, num)


do( '*', 10)