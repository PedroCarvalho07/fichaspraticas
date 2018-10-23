Lista1 = []
Max = 10

def par():
    for item in Lista1[0:Max]:
        if item % 2 == 0:
            print(item)
def impar():
    for item in Lista1[0:Max]:
        if item % 2 != 0:
            print(item)
for item in range(0,Max):
    item = int(input(" Escolha numero: "))
    Lista1.append(item)

parouimpar = input(" P ou I : ").title()

if parouimpar == 'P':
    par()
elif parouimpar =='I':
    impar()