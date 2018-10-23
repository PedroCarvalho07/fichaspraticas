A = []
B = []
C = []
D = []
E = []
Max = 10

def preencherA ():
    for item in range(0,Max):
        PerguntaA = int(input(" Escolha os valores para A: "))
        A.append(PerguntaA)

def preencherB ():
    for item in range(0,Max):
        PerguntaB = int(input("Escolha os valores para B: "))
        B.append(PerguntaB)

def preencherC ():
    for itemA in A:
        C.append(itemA)
    for itemB in B:
        C.append(itemB)

def preencherD ():
    for itemA in A:
        if itemA not in B:
            D.append(itemA)

def preencherE ():
    for itemA in A:
        if itemA in B:
            if itemA not in E:
                E.append(itemA)
    for itemB in B:
        if itemB not in E:
            E.append(itemB)

preencherA()
preencherB()
preencherC()
preencherD()
preencherE()

print(A)
print(B)
print(C)
print(D)
print(E)