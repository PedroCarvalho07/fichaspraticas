Saldobancario = int(input(" Escreva o seu saldo bancário "))
print(" 1 - Creditar ")
print(" 2 - Debitar ")
operação = int(input(" Escolha em cima se quer debitar ou creditar "))
montante = int(input(" Montante "))
if operação == 2 :
    saldoapos = Saldobancario - montante
    if saldoapos < 0 :
        print(" Operação impossível por saldo insuficiente ")
    else:
        print(" O saldo da sua conta bancaria é de {} €".format(saldoapos))
if operação == 1 :
    saldoapos = Saldobancario + montante
    print(" O saldo da sua conta bancaria é de {} €".format(saldoapos))
