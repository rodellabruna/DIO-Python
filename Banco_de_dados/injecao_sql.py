import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# documentação sqlite3: https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente:")
# não fazer desse jeito:
cliente = cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
# jeito correto de fazer:
liente = cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))
cliente = cursor.fetchone()
print(dict(cliente))