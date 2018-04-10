cordenadax = int(input( " Insira as coordenadas x :"))
cordenaday = int(input( " Insira as coordenadas y :"))

if cordenadax > 0:
    if cordenaday > 0:
        print (" As coordenadas pertencem ao primeiro quadrante")
elif cordenadax < 0:
    if cordenaday > 0:
        print (" As coordenadas pertencem ao segundo quadrante ")
elif cordenadax < 0:
    if cordenaday < 0: 
        print (" As coordenadas pertencem ao terceiro quadrante ")
elif cordenadax > 0:
    if cordenaday < 0:
        print (" As coordenadas pertencem ao quarto quadrante ")
elif cordenadax == 0:
    print (" As coordenadas estão no ponto de origem ")
elif cordenaday == 0:
    print (" As coordenadas estão no ponto de origem")