Nota1 = float(input( " Primeira Nota: "))
Nota2 = float(input( " Segunda Nota: "))
Nota3 = float(input( " Terceira Nota: "))

Médiafinal = ((Nota1 * 25 + Nota2 * 35 + Nota3 * 40)/100)

if Nota1 and Nota2 and Nota3 > 20:
    print(" Numero invalido")
elif Médiafinal >= 9.5:
    print(" O aluno está aprovado")
else:
    print(" O aluno está reprovado")