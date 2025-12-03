from pony.orm import Database, PrimaryKey, Required, Optional,db_session

db = Database()

class Pessoa(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    email = Required(str)
    telefone = Optional(str)

# Exemplo de bind (ajuste para seu banco real)
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

db.generate_mapping(create_tables=True)

#Criar uma pessoa:
with db_session:
    p = Pessoa(nome="Maria Silva", email="maria@example.com", telefone="11999998888")

#Consultar:
with db_session:
    pessoas = Pessoa.select()[:]
    print(pessoas)

#Atualizar:
with db_session:
    pessoa = Pessoa[1]
    pessoa.telefone = "11988887777"

#Deletar:
with db_session:
    Pessoa[1].delete()
