x = int(input(" Insira as respetivas coordenadas x: "))
y = int(input(" Insira as respetivas coordenadas y: "))

if x > 0:
    if y > 0:
        print(" As coordenadas pertencem ao primeiro Quadrante")
if x < 0:
    if y > 0:
        print(" As coordenadas pertencem ao segundo Quadrante")
if x < 0:
    if y < 0:
        print(" As coordenadas pertencem ao terceiro Quadrante")
if x > 0:
    if y < 0:
        print(" As coordenadas pertencem ao quarto Quadrante")
if x == 0:
    print(" A coordenada está no ponto de origem")
if y== 0:
    print(" A coordenada está no ponto de origem ")
