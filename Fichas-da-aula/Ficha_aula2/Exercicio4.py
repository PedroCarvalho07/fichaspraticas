x = int(input(" Insira as respetivas coordenadas x: "))
y = int(input(" Insira as respetivas coordenadas y: "))

if x > 0:
    if y > 0:
        print(" As coordenadas pertencem ao primeiro Quadrante")
elif x < 0:
    if y > 0:
        print(" As coordenadas pertencem ao segundo Quadrante")
elif x < 0:
    if y < 0:
        print(" As coordenadas pertencem ao terceiro Quadrante")
elif x > 0:
    if y < 0:
        print(" As coordenadas pertencem ao quarto Quadrante")
elif x == 0:
    print(" A coordenada está no ponto de origem")
elif y== 0:
    print(" A coordenada está no ponto de origem ")
