class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj) 
        
    
aluno1 = Estudante("Guilherme", 1)
aluno2 = Estudante ("Giovanna", 2)
mostrar_valores(aluno1,aluno2)

Estudante.escola = "Python"
aluno1.matrcula = 3
aluno3 = Estudante("Chappie", 4)
mostrar_valores(aluno1,aluno2,aluno3)

