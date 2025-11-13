import sqlite3

conn = sqlite3.connect('bancoricio.db')
cursor = conn.cursor()

class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS contatos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         email TEXT NOT NULL,
#         telefone TEXT NOT NULL
#     )                          
# ''')

ctt1 = Contato('Mauricio', 'mauricio@gmail.com', '41987282408')
ctt2 = Contato('Debora', 'mauro@gmail.com', '41999703924')

# cursor.execute(
#     "INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)",
#     (ctt1.nome, ctt1.email, ctt1.telefone)
# )

# cursor.execute(
#     "INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)",
#     (ctt2.nome, ctt2.email, ctt2.telefone)
# )

# cursor.execute(
#     "UPDATE contatos SET telefone = ? WHERE nome = ?",
#     ('41999346587', 'Mauricio')
# )

# cursor.execute(
#     "UPDATE contatos SET email = ? WHERE nome = ?",
#     ('debora@gmail.com', 'Debora')
# )

# cursor.execute(
#     "DELETE FROM contatos WHERE nome = ?",
#     ('Debora',)
# )

cursor.execute("SELECT * FROM contatos")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

conn.commit()
