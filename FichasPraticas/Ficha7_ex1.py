class Aluno():

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return "O aluno {} tem o nome {}".format(self.nome, self.numero.title())
    

A1 = Aluno(1, "Pedro")
print(A1)
A2 = Aluno(2, "Carvalho")
print(A2)