from abc import ABC, abstractmethod, abstractproperty

#classe instanciada não pode ser acessada diretamente

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligar a TV")
        print("TV ligada")
        
    def desligar(self):
        print("Desligar a TV")
        print("TV desligada")
    
    @property
    def marca(self):
        return "LG"
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligar o ar condicionado")
        
    def desligar(self):
        print("Ar condicionado desligado")
        
    @property
    def marca(self):
        return "Samsung"

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle2 = ControleArCondicionado()
controle2.ligar()
controle2.desligar()
print(controle2.marca)

