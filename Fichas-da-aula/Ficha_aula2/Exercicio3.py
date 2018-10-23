Numero1 = int(input(" Escolha o primeiro numero: "))
Numero2 = int(input(" Escolha o segundo numero: "))
Operacao = input(" Escolha a opçao que deseja realizar : +-*/ ")

if Operacao == "+":
        resultado=(Numero1 + Numero2)
elif Operacao == "-":
        resultado=(Numero1 - Numero2)
elif Operacao == "*":
        resultado=(Numero1 * Numero2)
elif Operacao == "/":
        resultado=(Numero1 / Numero2)

print(" o resultado é :", resultado)


