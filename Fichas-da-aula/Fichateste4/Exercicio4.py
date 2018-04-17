def imprimir_números(numero) :
    if numero >= 0:
        imprimir_números(numero - 1)
        print(numero, end=" ")

numero=int(input("Inserir número máximo: "))

imprimir_números(numero)