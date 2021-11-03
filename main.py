import sqlite3

banco = sqlite3.connect("mydb.db", 100)
print("...Arquivo criado com sucesso!")
cur = banco.cursor()
cursor = cur
def conexao():
  try:
    cursor= banco.cursor()
    cursor.connection == banco
    print("Banco conectado!")
  except ConnectionError:
    print("Erro de conexão!")
conexao()



def CriarTabela():
  try:
    cursor = cur
    cursor.execute("CREATE TABLE dados(id integer primary key, nome text, idade integer, email text)")
    print("Tabela criada com sucesso!")
  except Exception:
    print("Erro na criação de tabelas!")
  
def InsertData():
  try:
    lista = [(1,"Carlos",22,"carlos22@gmail.com")]
    cursor = cur
    cursor.executemany("insert into dados values(?,?,?,?)", lista)
    print(lista, "\nDados inseridos com sucesso!")
  except:
    print("Dados não inseridos!")

def Deletar():
  x = int(input("Digite o número da linha que deseja deletar: "))
  try:
    cursor = cur
    cursor.execute("Delete from dados where id=:row ", {"row": x})
    print("Linha", x , " foi deletada com sucesso")
    exibir()
  except:
    print("Erro ao deletar linha!")

#CriarTabela()
#InsertData()
def exibir():
  cursor = cur
  cursor.execute("select * from dados where id=:number", {"number": 1})
  for row in cursor:
    print(row)
#Deletar()
exibir()
banco.commit()
banco.close()