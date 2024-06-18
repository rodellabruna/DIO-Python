# # TODO: Crie uma classe UsuarioTelefone.  
# # TODO: Defina um método especial `__init__`, que é o construtor da classe.
# # O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.


        
#     # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.

# class UsuarioTelefone:
#     def __init__(self, nome, numero, plano):
#         self.nome = nome
#         self.numero = numero
#         self.cpf = plano

#     # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
#     def __str__(self):
#         return f"Usuário {self.nome} criado com sucesso."


# # Entrada:
# nome = input()  
# numero = input()  
# plano = input()  
# # TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

# usuario = UsuarioTelefone(nome, numero, plano)

# print(usuario)


# # TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
# class PlanoTelefone:
#     def __init__(self, nome, saldo):
#         self._nome = nome
#         self._saldo = saldo

# # TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:
#     def get_saldo(self):
#         return self._saldo    
    
# # TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:
#     def mensagem_personalizada(self):
#         if self.get_saldo() < 10:
#             return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
#         elif self.get_saldo() >= 50:
#             return "Parabéns! Continue aproveitando seu plano sem preocupações."
#         else:
#             return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
 
# # Classe UsuarioTelefone:
# class UsuarioTelefone:
#     def __init__(self, nome, plano):
#         self.nome = nome
#         self.plano = plano

# # TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
#     def verificar_saldo(self):
#         saldo = self.plano.get_saldo()
#         mensagem = self.plano.mensagem_personalizada()
#         return saldo, mensagem        


# # Recebendo as entradas do usuário (nome, plano, saldo):
# nome_usuario = input()
# nome_plano = input()
# saldo_inicial = float(input())

#  # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
# plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
# usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# # Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
# saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
# print(mensagem_usuario)





