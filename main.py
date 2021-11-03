import sqlite3

banco = sqlite3.connect("banco2.db")
#print("Um novo arquivo foi criado!")
cursor = banco.cursor()
def conexao():
  cursor = banco.cursor()
  if cursor.connection == banco:
    print("Conexão funcionando!")
  else:
    print("Falha na conexão!")

def criarTabela():
  try:
    cursor.execute("create table dados(id integer primary key, nome text, idade integer)")
    print("Tabela criada com sucesso!")
  except:
    print("Não possível criar a tabela! :/")

def inserirDados():
  try:
    linha = int(input("Digite o id: "))
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    cursor.execute("insert into dados VALUES(?,?,?)",(linha, nome, idade))
    print("Dados foram inseridos com sucesso!")
  except:
    print("Os dados não foram inseridos!")

def deletaDados():
  try:
    N = int(input("Digite um número: "))
    cursor.execute("delete from dados where id=:Numero",{"Numero": N})
    print("Dados deletados com sucesso!")
  except:
    print("Dados não foram deletados! :(")

def atualizaDados():
  try:
    novoNome = str(input("Digite o nome: "))
    posicao = int(input("Digite um número: "))
    cursor.execute("update dados set nome =:name where id=:Posicao",{"name":novoNome,"Posicao":posicao})
    print("Dados from atualizados com sucesso!")
  except:
    print("Dados não foram atualizados! :(")

def exibirDados():
  number = [0,1,2,3]
  while True:
    opcoes = int(input("Digite a opção que deseja exibir(0 até 3): "))
    if number[0] == opcoes:
      for row in cursor.execute("select * from dados"):
        print(row)
    elif number[1] == opcoes:
      for row in cursor.execute("select id from dados"):
        print(row)
    elif number[2] == opcoes:
      for row in cursor.execute("select nome from dados"):
        print(row)
    else:
      for row in cursor.execute("select idade from dados"):
        print(row)
#inserirDados()
#conexao()
#criarTabela()
#inserirDados()
#deletaDados()
atualizaDados()
exibirDados()
print(cursor.fetchone()[1])
banco.commit()
banco.close()