from Ficha7_ex1 import Aluno

class Turma():

    def __init__(self, nome, ano):
        self.nome_turma = nome
        self.ano_letivo = ano
        self.lista_alunos = []
        self.total_alunos = 0

    def __str__(self):
        return "Nome da turma {} \n Ano letivo {} \n Número de alunos {} \n Lista de alunos {}".format(self.nome_turma, self.ano_letivo, self.total_alunos, self.lista_alunos)

    def verifica_aluno(self, aluno):
        for i in range(self.total_alunos):
            if self.lista_alunos[i].e_igual(aluno):
                return True
            return False

    def insere_instancia_aluno(self, aluno):
        if self.verifica_aluno(aluno) == False:
            self.lista_alunos.append(aluno)
            self.total_alunos += 1
            return True
        return False

T1 = Turma("CRSI","2017/2018")
print(T1)