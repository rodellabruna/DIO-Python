def meu_decorador(funcao):
    def envelope():
        print("fal algo antes de executar")
        funcao()
        print("faz algo depois de executar")
        
    return envelope

@meu_decorador
def ola_mundo():
    print("Olá, mundo!")

ola_mundo()
