num_1 = int(input(" Escolha o primeiro numero :"))
num_2 = int(input(" Escolha o segundo numero :"))
operação = input (" Escolha a operação que deseja realizar : +-*/ ")

if operação == "+" :
    resultado= num_1 + num_2
elif operação == "-" :
    resultado== num_1 - num_2
elif operação == "*" :
    resultado== num_1 * num_2
elif operação == "/" :
    resultado== num_1 / num_2

print(" o resultado é :", resultado)   