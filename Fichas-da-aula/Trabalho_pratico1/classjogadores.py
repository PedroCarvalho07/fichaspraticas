class Jogador(): #Classe do Jogador

    def __init__(self): #Iniciar a funcao para chamar o nome e o token sozinhos
        self.nome = None #O none faz com que o espaço para o nome esteja completamente vazio
        self.token = None #O none faz com que o espaço para o nome esteja completamente vazio

#DadosJogador 1
jogador1 = Jogador() #Igualar o jogador2 há variável jogador 
jogador1.nome = input(" Insira o nome do jogador1: ") #Pede o nome do jogador1
jogador1.token = input(" Insira o token que deseja dar ao jogador1: ") #Pede o token ao jogador

#DadosJogador 2
jogador2 = Jogador() #Igualar o jogador2 há variável jogador 
jogador2.nome = input(" Insira o nome do jogador2: ") #Pede o nome do jogador1

jogador2.token = jogador1.token

while jogador1.token == jogador2.token: #Igualamos o token 1 ao token 2
      jogador2.token = input(" Insira o token que deseja dar ao jogador 2: ")   
      
print (" Jogador1 chama-se {} e escolheu o token {} para jogar " .format(jogador1.nome,jogador1.token)) #Assume o nome do jogador1 e o token1
print (" Jogador2 chama-se {} e escolheu o token {} para jogar " .format(jogador2.nome,jogador2.token)) #Assume o nome do jogador2 e o token2


