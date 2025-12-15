# service.py
from pony.orm import db_session, select
from model_person import Pessoa  # importa a Entity do arquivo models.py

# -----------------------------
# CREATE
# -----------------------------
@db_session
def insert(nome, email, telefone):
    pessoa = Pessoa(nome=nome, email=email, telefone=telefone)
    return {"result": "ok", "details": pessoa.id}


# -----------------------------
# DELETE
# -----------------------------
@db_session
def delete(pessoa_id):
    pessoa = Pessoa.get(id=pessoa_id)
    if not pessoa:
        return {"result": "ok", "details": 0}

    pessoa.delete()
    return {"result": "ok", "details": 1}


# -----------------------------
# UPDATE
# -----------------------------
@db_session
def update(pessoa_id, nome=None, email=None, telefone=None):
    pessoa = Pessoa.get(id=pessoa_id)
    if not pessoa:
        return {"result": "ok", "details": 0}

    if nome is not None:
        pessoa.nome = nome
    if email is not None:
        pessoa.email = email
    if telefone is not None:
        pessoa.telefone = telefone

    return {"result": "ok", "details": 1}


# -----------------------------
# RETRIEVE ALL
# -----------------------------
@db_session
def retrieveAll():
    pessoas = select(p for p in Pessoa)[:]  # lista real

    result = [
        {
            "id": p.id,
            "nome": p.nome,
            "email": p.email,
            "telefone": p.telefone or ""
        }
        for p in pessoas
    ]

    return {"result": "ok", "details": result}


# -----------------------------
# RETRIEVE BY ID
# -----------------------------
@db_session
def retrieveById(pessoa_id):
    p = Pessoa.get(id=pessoa_id)
    if not p:
        return {"result": "not_found", "details": None}

    pessoa = {
        "id": p.id,
        "nome": p.nome,
        "email": p.email,
        "telefone": p.telefone or ""
    }

    return {"result": "ok", "details": pessoa}
