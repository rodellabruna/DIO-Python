class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2022 - self._ano_nascimento
    
pessoa = Pessoa("Guilherme",1994)
print(f"Nome: {pessoa.nome} \t Idade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()} \t Idade: {pessoa.get_idade()}")