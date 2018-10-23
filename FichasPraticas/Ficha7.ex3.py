from Ficha7_ex1 import Aluno
from Ficha7_ex2 import Turma

def inserir_instancia_aluno(turma, aluno):
    if(turma.insere_instancia_aluno(aluno)):
        return "Aluno inserido com sucesso"
    return "Aluno não inserido, verifique os dados"

def inserir_aluno(turma, numero, nome):
    aluno = Aluno(numero, nome)
    if(turma.insere_instancia_aluno(aluno)):
        return "Aluno inserido com sucesso"
    return "Aluno não inserido, verifique os dados"

def obter_aluno(turma, posicao):
    if turma.retorna_aluno(posicao) == None:
        return "Não existe nenhum aluno nessa posição"
    return turma.retorna_aluno(posicao)


# Criar alunos
aluno_1 = Aluno(859213, "jorge figueiredo")
aluno_2 = Aluno(859242, "pedro santos")

# Criar turma
crsiT2 = Turma("CRSI T2", "2017/18", 2)

# inserir alunos
print(inserir_instancia_aluno(crsiT2, aluno_1))
print(inserir_instancia_aluno(crsiT2, aluno_2))
print(inserir_aluno(crsiT2, 859213, "jose bonifacio"))

# 3 a)
crsiT2.marcar_presenca(aluno_1, 1)
crsiT2.marcar_presenca(aluno_2, 1)
crsiT2.marcar_presenca(aluno_2, 2)

# 3 b)
print(crsiT2.imprime_folha_presencas())

# 3 c)
print(crsiT2.imprime_folha_presencas_dia(1))