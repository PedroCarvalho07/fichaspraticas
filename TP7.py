class Aluno():

    def __init__(self, numero, nome):
        self.numerodoaluno = numero
        self.nomedoaluno = nome.title()

    def _str_(self):
        return "Numero: {} | Nome: {}".format(self.numerodoaluno,self.nomedoaluno)

class Turma():

    def __init__(self, nome, ano):
        self.turma = nome
        self.anoletivo = ano
        self.listadealunos = []
        self.totaldealunos = 0

    def verificação_existe(self, aluno):
        for i in range(self.totaldealunos):
            if self.listadealunos[i].e_igual(aluno):
                return True
            return False
    
    def insere_instancia_aluno(self, aluno):
        if  self.verificação_existe(aluno) == False:
            self.listadealunos.append(aluno)
            self.totaldealunos += 1
            return True
        return False

    def inserir_aluno(self, nome, numero):
        aluno = Aluno(numero, nome)
        return self.insere_instancia_aluno(aluno(nome,numero))
    
