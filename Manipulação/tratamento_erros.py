from pathlib import Path

try:
    arquivo = open("meu-arquivo.txt")
except FileNotFoundError as exc:
    print("Arquivo não encontrado")
    print(exc)
    
ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except Exception as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")