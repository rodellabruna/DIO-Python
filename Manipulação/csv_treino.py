import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
COLUNA_ID = 0
COLUNA_NOME = 1

try: 
    with open (ROOT_PATH / "usuarios.csv", "a ", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["3", "Maria"])
        escritor.writerow(["4", "João"])
except Exception as exc:
    print(f"Erro ao criar o arquivo: {exc}")


# try: 
#     with open (ROOT_PATH / "usuarios.csv", "r", encoding="utf-8", newline='') as arquivo:
#         leitor = csv.reader(arquivo)
#         for idx, row in enumerate(leitor):
#             if idx == 0:
#                 continue
#             print(f'ID: {row[COLUNA_ID]}')
#             print(f'Nome: {row[COLUNA_NOME]}')
# except Exception as exc:
#     print(f"Erro ao ler o arquivo: {exc}")
    
# try: 
#     with open (ROOT_PATH / "usuarios.csv", newline='', encoding="utf-8") as arquivo:
#         reader = csv.DictReader(arquivo)
#         for row in reader:
#             print(row["id"], row["nome"])
# except Exception as exc:
#     print(f"Erro ao ler o arquivo: {exc}")