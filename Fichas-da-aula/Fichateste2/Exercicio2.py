Numero1 = int(input(" Escolher o primeiro numero: "))
Numero2 = int(input(" Escolher o segundo numero: "))
Numero3 = int(input(" Escolher o terceiro numero: "))

if Numero1 > Numero2 > Numero3:
    print( Numero1,Numero2,Numero3)
elif Numero2 > Numero3 > Numero1:
    print( Numero2,Numero3,Numero1)
elif Numero3 > Numero2 > Numero1:
    print( Numero3, Numero2,Numero1)
elif Numero1 > Numero3 > Numero2:
    print(Numero1,Numero3,Numero2)
elif Numero2 > Numero1 > Numero3:
    print(Numero2,Numero1,Numero3)
elif Numero3 > Numero1 > Numero2:
    print(Numero3,Numero1,Numero2)
    