"Escolha 5 numeros há sua escolha :"
num_1 = int(input(" Escolha o primeiro numero :"))
num_2 = int(input(" Escolha o segundo numero :"))
num_3 = int(input(" Escolha o terceiro numero :"))
num_4 = int(input(" Escolha o quarto numero :"))
num_5 = int(input(" Escolha o quinto numero :"))

Média = float( num_1 + num_2 + num_3 + num_4 + num_5 )/5
Parteinteira = int( num_1 + num_2 + num_3 + num_4 + num_5 )//5
Modulodedivisao = ( num_1 + num_2 + num_3 + num_4 + num_5 )%100
print(" O resultado é: ", Média)
print(" O resultado é: ", Parteinteira)
print(" O resultado é: ", Modulodedivisao)