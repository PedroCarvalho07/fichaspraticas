Numero1 = int(input(" Escolha um numero: "))
Numero2 = int(input("Escolha um numero :"))
Operacao = input( " Escolha a opcao que deseja realizar: +-*/ ")

if Operacao == '+':
    resultado = (Numero1 + Numero2)
elif Operacao == '-':
    resultado = (Numero1 - Numero1)
elif Operacao == '*':
    resultado = (Numero1 * Numero2)
elif Operacao == '/':
    resultado = (Numero1 / Numero2)

print (" O resutado é :", resultado)    