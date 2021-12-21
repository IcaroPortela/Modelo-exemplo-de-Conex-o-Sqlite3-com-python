import sqlite3
from sqlite3.dbapi2 import Cursor
def conexao():
    try:
        db = sqlite3.connect('teste.db')
        Cursor.cursor = db.cursor()
        print("Conectado")
    except:
        print("Não foi possível se conectar")

conexao()

def criarTabela():
    Cursor.cursor.execute("CREATE TABLE pessoa (nome text, idade integer, email text)")

criarTabela()

def Cadastro():
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade'))
#cursor.execute(f"INSERT INTO pessoa ('{nome}', '{idade}', '{email}'")
Cursor.cursor.execute("UPDATE pessoa SET nome = 'Icaro' WHERE idade = 28")
Cursor.cursor.execute("SELECT * FROM pessoa")
print(Cursor.cursor.fetchall())
conexao.db.commit()

#pyinstaller --windowed 'nome do arquivo .py'
#copiar o arquivo .ui ou de exibição para a pasta dist
