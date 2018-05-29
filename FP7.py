import random

file = open ("teste.txt", "a")

NUM_VALOR = 30
NUM_MAXIMO = 100

for i in range(0,NUM_VALOR):
    a = str((random.randint(1,NUM_MAXIMO)) + "\n" )
    file.write(a)
file.close ()    
