limite = int(input(" Introduza a variavel limite do ciclo: "))
salto = int(input(" Introduza o salto do ciclo: "))

for item in range (0, limite, salto) :
    print(item)