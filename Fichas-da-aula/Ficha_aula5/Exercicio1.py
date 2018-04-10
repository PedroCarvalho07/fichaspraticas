def quatro_linhas(): #define a função quatro_linhas sem argumentos
    linha_quadrado() #que chamará a função linha_quadrado quatro vezes.
    linha_quadrado()
    linha_quadrado()
    linha_quadrado()
    
def Linha_quadrado(): #define uma função para desenhar uma linha do quadrado
    print( '+','- ' *4,'+', '- ' * 4, '+' )

def linha_quadrado(): #define uma função para desenhar uma linha mais simples do quadrado
    print ('|', ' ' * 8, '|', ' ' *8, '|') 

def quadrado(): #define a função que formará o quadrado, juntando as linhas     
    Linha_quadrado()
    quatro_linhas()
    Linha_quadrado()
    quatro_linhas()
    Linha_quadrado()

quadrado() #chama a função que desenha o quadrado