class Aluno():    
    def __init__(self, nome, numero, data_nascimento):
        self.nome = nome
        self.numero = numero
        self.data_nascimento = data_nascimento
        self.nota = 0
        self.quantidade = 0
        self.media = 0

    def adnota(self, adicionar_nota):
        if  adicionar_nota >=0:
            self.nota = self.nota + adicionar_nota
            self.quantidade = self.quantidade + 1
    
    def final(self):
        self.media = self.nota / self.quantidade

    def __str__ (self):
        return " Numero: {}\nNome:  {}\nData: {}".format(self.nome, self.numero, self.data_nascimento)

aluno1 = Aluno(1, " Diogo", "13 de Maio de 1990")
aluno1.adnota(20)
aluno1.adnota(18)
aluno1.final()
print(aluno1)
print(aluno1.nota)
print(" Media aluno 1: ", aluno1.media)

aluno2 = Aluno(2, "Luis", " 13 de Maio de 1234")
aluno2.adnota(12)
aluno2.adnota(4)
aluno2.final()
print(aluno2)
print(aluno2.nota)
print(" Media aluno 2: ", aluno2.media)


    
