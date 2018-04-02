voto=int(input("Insira o seu voto (1, 2, 3 ,4), (0 se for voto nulo), (9 se for voto em branco) e (-1 para terminar a eleição) : "))
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
voto_branco = 0
voto_nulo = 0
while voto != -1:
    if voto == 1:
        candidato_1 += 1
    if voto == 2:
        candidato_2 += 1
    if voto == 3:
        candidato_3 += 1
    if voto == 4:
        candidato_4 += 1
    if voto == 0:
        voto_branco += 1
    if voto == 9:
        voto_nulo += 1
    voto=int(input("Insira o seu voto (1, 2, 3 ,4), (0 se for voto nulo), (9 se for voto em branco) e (-1 para terminar a eleição) : "))

totalvotos= candidato_1 + candidato_2 + candidato_3 + candidato_4 + voto_nulo + voto_branco
percentagem_candidato1 = (candidato_1 * 100) / totalvotos
percentagem_candidato2 = (candidato_2 * 100) / totalvotos
percentagem_candidato3 = (candidato_3 * 100) / totalvotos
percentagem_candidato4 = (candidato_4 * 100) / totalvotos
percentagem_branco = (voto_nulo * 100) / totalvotos
percentagem_nulo = ( voto_branco * 100) / totalvotos

print("O total de votos desta eleição são : {}".format(totalvotos))
print("O total de votos para o candidato 1 são : {}".format(candidato_1))
print("O total de votos para o candidato 2 são : {}".format(candidato_2))
print("O total de votos para o candidato 3 são : {}".format(candidato_3))
print("O total de votos para o candidato 4 são : {}".format(candidato_4))
print("O total de votos em branco são : {}".format(voto_branco))
print("O total de votos nulos são : {}".format(voto_nulo))
print("A percentagem de votos para o candidato 1 são : {} %".format(percentagem_candidato1))
print("A percentagem de votos para o candidato 2 são : {} %".format(percentagem_candidato2))
print("A percentagem de votos para o candidato 3 são : {} %".format(percentagem_candidato3))
print("A percentagem de votos para o candidato 4 são : {} %".format(percentagem_candidato4))
print("A percentagem de votos em branco são : {} %".format(percentagem_branco))
print("A percentagem de votos nulos são : {} %".format(percentagem_nulo))