Nota1 = float(input(" Escreva a primeira nota "))
Nota2 = float(input(" Escreva a segunda nota "))
Nota3 = float(input(" Escreva a terceira nota "))

Media = float((Nota1 * 25 + Nota2 * 35 + Nota3 * 40)/100)
Mediainteria = int((Nota1 * 25 + Nota2 * 35 + Nota3 * 40) //100)
mediamodulo = int((Nota1 * 25 + Nota2 * 35 + Nota3 * 40)%100)

print(" A sua média sera {}, a media interia tem o valor de {} e a sua media modulo e {}".format(Media,Mediainteria,mediamodulo))
