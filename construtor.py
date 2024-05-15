class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a estrutura...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instancia da classe")
        
    def falar(self):
        print("auau")
        
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie","Amarelo")
# c.falar()

#criar_cachorro()

print("Ola Mundo")
del c
print("Ola Mundo")
print("Ola Mundo")
print("Ola Mundo")
