Coordenadax = int(input(" Introduza a coordenada x :"))
Coordenaday = int(input(" Introduza a coordenada y :"))

if Coordenadax > 0:
    if Coordenaday > 0:
        print (" Pertence ao primeiro Quadrante")
elif Coordenadax > 0:
    if Coordenaday < 0:
        print (" Pertence ao segundo Quadrante")
elif Coordenadax < 0:
    if Coordenaday < 0:
        print (" Pertence ao terceiro Quadrante")
elif Coordenadax < 0:
    if Coordenaday > 0:
        print (" Pertence ao quarto Quadrante")
elif Coordenadax == 0:
    if Coordenaday == 0:
        print (" Está no ponto de origem")