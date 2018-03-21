Numero1 = int(input(" Digite o seu numero: "))

if Numero1 % 3 == 0 and Numero1 % 5 == 0:
    print(" O seu numero {} é divisivel por 3 e por 5".format(Numero1))
else:
    print(" O seu numero {} não é divisivel por 3 e por 5".format(Numero1))