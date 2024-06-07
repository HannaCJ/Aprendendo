#objetivo era treinar classes e funções, adicionando alunos e turmas em sala de aula
class Aluno: #para adicionar alunos
    totalAlunos=0 #contador para alunos
    def __init__ (self,nome,nota):  #3 parâmetros 
        Aluno.totalAlunos+=1 #aumenta o total de alunos sempre q for adicionado um aluno novo
        self.nome =nome #nome do aluno
        self.nota = nota # notas do aluno
        self.ru=1000+ Aluno.totalAlunos #atribui um Registro único de acada aluno

    def info(self): #para adicionar informações dos alunos
        print(f' Nome: {self.nome}; RU: {self.ru}; Nota: {self.nota};')

    def getNota(self): #get sao metodos q retornam valores, nesse caso retornará a nota do aluno
        return self.nota
#a1= Aluno('Mario',90)
#a1.info()

class Turma:
    def __init__ (self, nome, limiteAlunos):
        self.nome=nome #definindo nome da turma
        self.limiteAlunos=limiteAlunos #limite de alunos por turma
        self.listaAlunos=[] #iniciando uma lista vazia para os alunos da turma

    def addAluno(self,aluno):
        if len(self.listaAlunos) < self.limiteAlunos: #verificando se a turma não atingiu limite máximo de alunos
            self.listaAlunos.append(aluno) #add aluno na lista
            return True
        return False

    def mediaTurma(self): #calcula a média da turma
        soma=0 #soma das notas
        for aluno in self.listaAlunos:
            soma+=aluno.getNota()
        return soma/len(self.listaAlunos) #retorna a média
a1 = Aluno('Mario', 90)
a2 = Aluno('Luigi', 80)
a3 = Aluno('Yoshi', 40)

t1= Turma('Programação', 2)  #cria a turma Programação e um limite de 2 alunos na turma
t1.addAluno(a1) #adicionando alunos na turma
t1.addAluno(a2)
t1.addAluno(a3)
t1.addAluno(Aluno('Peach',100))
print(t1.mediaTurma())  # a media so sai dos dois primeiros alunos, pq o limite pra turma sao 2 alunos
print(t1.listaAlunos[0].getNota()) #imprimindo a nota do aluno Mario
