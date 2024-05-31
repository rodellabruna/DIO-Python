from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(ROOT_PATH)

try:
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
        print(arquivo.read()) #garante o fechamento do arquivo
        print("=" * 20)

except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
    print("=" * 20)

#print(arquivo.read()) => não vai funcionar aqui fora do with

# try:
#     with open(ROOT_PATH / 'arquivo-utf-8.txt', 'w', encoding='utf-8') as arquivo:
#         arquivo.write("Manipulando arquivos usando Pyhton")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo: {exc}")

try:
    with open(ROOT_PATH / 'arquivo-utf-8.txt', 'r', encoding='ascii') as arquivo:
        print(arquivo.read())
except Exception as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
    print("=" * 20)