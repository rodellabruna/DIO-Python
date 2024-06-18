import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# documentação sqlite3: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ('Teste 7', 'teste7@gmailcom'))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2,'Teste 8', 'teste8@gmailcom'))
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ('Teste 9', 'teste9@gmailcom'))
    conexao.commit()
except Exception as exc:
    print(f"Ops! Ocorreu um erro! {exc}")
    conexao.rollback()
# finally:
#    conexao.commit()

# outra forma - escreve o with e coloca todo o código como um bloco:
# with sqlite3.connect(ROOT_PATH /"meu_banco.sqlite") as conexao: