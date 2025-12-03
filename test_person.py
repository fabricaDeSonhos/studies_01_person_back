# remove the database file
import os
if os.path.exists('database.sqlite'):
    os.remove('database.sqlite')

from model_person import *

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
