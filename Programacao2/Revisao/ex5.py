Numero1 = int(input(" Escolha o primeiro numero: "))
Numero2 = int(input(" Escolha o segundo numero: "))

print(" Escolha a seguinte opcao que deseja efetuar: ")
print(" 1- Soma")
print(" 2- Subtracao")
print(" 3- Multiplicacao")
print(" 4-Divisao")
opcao = int(input("Opcao: "))

def soma (Numero1,Numero2):
    res = (Numero1 + Numero2)
    return res
def Subtracao (Numero1, Numero2):
    res = (Numero1 - Numero2)
    return res
def Multiplicacao (Numero1, Numero2):
    res = (Numero1 * Numero2)
    return res
def Divisao (Numero1, Numero2):
    res = (Numero1, Numero2)
    return res
if opcao == 1:
    res = soma(Numero1,Numero2)
    print(res)
elif opcao == 2:
    res = Subtracao(Numero1, Numero2)
    print(res)
elif opcao == 3:
    res = Multiplicacao(Numero1, Numero2)
    print(res)
elif opcao == 4:
    res = Divisao(Numero1, Numero2)
    print(res)