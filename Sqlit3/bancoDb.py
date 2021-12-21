import sqlite3

db = sqlite3.connect('cadastro.db') # cria um banco de dados
cursor = db.cursor() #agrega o banco 
cursor.execute("CREATE TABLE alunos (nome text, matricula integer, data text)")
cursor.execute("INSERT INTO alunos VALUES('Maria',0001,'16/07/2021')")
cursor.execute("DELETE from alunos WHERE matricula = 1")
db.commit()

def exibirDados():
    cursor.execute("SELECT * FROM alunos")
    print(cursor.fetchall())

exibirDados()