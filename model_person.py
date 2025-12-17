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

