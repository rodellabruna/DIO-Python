import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# documentação sqlite3: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));'
        )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()
    
    
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?);', dados)
    conexao.commit()
    
def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")
    
    
def recuperar_clientes(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

    
def recuperar_clientes_2(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


cliente = recuperar_clientes_2(cursor, 3)
print(dict(cliente))
print(cliente["nome"], cliente["id"])
print("Lista:")
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))
    
print(f'Seja bem vindo ao sistema {cliente["nome"]}')
print(f'Seja bem vindo ao sistema {cliente[1]}')
    
# dados = [
#     ("Thiago", "thiago@gmail.com"),
#     ("Aline", "aline@gmail.com"),
#     ("Karina", "karina@gmail.com"),
#     ("Pedro", "pedro@gmail.com")   
# ]

# atualizar_registro(conexao, cursor, "Guilherme", "guilherme@gmail.com", 2)
# atualizar_registro(conexao, cursor, "Guilherme Andrade", "guilherme@gmail.com", 2)

# excluir_registro(conexao, cursor, 2)

# inserir_muitos(conexao, cursor, dados)