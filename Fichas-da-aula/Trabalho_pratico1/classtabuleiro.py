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



#Dados Class Tabuleiro
class tabuleiro():
    
    def __init__(self):

        self.tabuleiro = [ [None, None, None], 
                           [None, None, None], 
                           [None, None, None] ]

#Definir uma funcao para a criação do tabuleiro
    def __str__(self):
        tab = "\n  A|B|C"
        for j in range (0, 3):
            tab += "\n" + str(j+1) + "|"
            for i in range (0, 3):
                if self.tabuleiro[j][i] == None:
                    tab += " |"
                else:
                    tab += self.tabuleiro[j][i] + "|"
        return tab

#Definir uma funcao para podermos validar a jogada com as respetivas coordenadas    
    def validarjogada(self,jogada,token):        
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            if jogada[0] == "A":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Por favor escolha outra casa")
                    jogada = input("Jogue entre as respetivas casas (A1 - C3) ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "B":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Por favor escolha outra casa")
                    jogada = input("Jogue entre as respetivas casas (A1 - C3) ")
                    self.validarjogada(jogada,token)
            if jogada[0] == "C":
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == None:
                    self.tabuleiro[linha][coluna] = token
                else:
                    print("Por favor escolha outra casa")
                    jogada = input("Jogue entre as respetivas casas (A1 - C3)")
                    self.validarjogada(jogada,token)
        else:
            print("Por favor escolha outra casa")
            jogada = input("Jogue entre as respetivas casas (A1 - C3):  ")
            self.validarjogada(jogada,token)

#Retirado do github do jogo da Velha
#Esta função permite verificar se existe vencedor do jogo
   
    def vitoria(self,nome,token):
        if  (self.tabuleiro[0][0] == token and self.tabuleiro[0][1] == token and self.tabuleiro[0][2] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][0] == token and self.tabuleiro[2][0] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[0][2] == token):
            global winner
            winner = True
        return winner

tabuleiro1 = tabuleiro()    
tabuleiro1.__str__()

print(tabuleiro1)
winner = False
while jogadas_max < 9:
    jogada = input("{}, que jogada pretende fazer (A1 - C3)? Se pretender desistir digite exit:   ".format(jogador1.nome))
    if jogada == "exit":
        print("Como o jogador {} desistiu temos como vencedor o jogador {}  ".format(jogador1.nome,jogador2.nome))
        break
    tabuleiro1.validarjogada(jogada,jogador1.token)
    print(tabuleiro1)
    tabuleiro1.vitoria(jogador1.nome,jogador1.token)
    if winner == True:
        print("O vencedor deste jogo é o :",jogador1.nome)
        break
    jogadas_max += 1
    if jogadas_max == 9:
        print("Temos um empate")
        break
    jogada = input("{}, que jogada pretende fazer (A1 - C3)? Se pretender desistir digite exit: ".format(jogador2.nome))
    if jogada == "exit":
        print("Como o jogador {} desistiu temos como vencedor o jogador {}  ".format(jogador2.nome,jogador1.nome))
        break
    tabuleiro1.validarjogada(jogada,jogador2.token)
    print(tabuleiro1)
    tabuleiro1.vitoria(jogador2.nome,jogador2.token)
    if winner == True:
        print("O vencedor deste jogo é o : ",jogador2.nome) 
        break
    jogadas_max += 1
