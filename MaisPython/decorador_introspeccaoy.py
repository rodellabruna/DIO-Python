import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá, mundo {nome}!")


resultado = ola_mundo("João")
print(resultado)
print(ola_mundo.__name__)
