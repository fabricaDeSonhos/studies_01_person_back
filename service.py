# pessoas_service.py

# Base estática (dados simulados)
_FAKE_PESSOAS = [
    {"id": 1, "nome": "john",  "email": "john@gmail.com",  "telefone": "912345678"},
    {"id": 2, "nome": "maria", "email": "maria@gmail.com", "telefone": ""},
    {"id": 3, "nome": "carla", "email": "carla@exemplo.com", "telefone": "11988887777"},
]

def insert(nome, email, telefone):
    """Insere uma pessoa (simulado)."""
    return {"result": "ok", "details": 3}  # ID gerado fixo

def delete(pessoa_id):
    """Exclui uma pessoa (simulado)."""
    deleted = 1 if pessoa_id in (1, 2, 3) else 0
    return {"result": "ok", "details": deleted}

def update(pessoa_id, nome=None, email=None, telefone=None):
    """Atualiza uma pessoa (simulado)."""
    updated = 1 if pessoa_id in (1, 2, 3) else 0
    return {"result": "ok", "details": updated}

def retrieveAll():
    """Retorna todas as pessoas (simulado)."""
    return {"result": "ok", "details": _FAKE_PESSOAS}

def retrieveById(pessoa_id):
    """Retorna uma pessoa pelo ID (simulado)."""
    for pessoa in _FAKE_PESSOAS:
        if pessoa["id"] == pessoa_id:
            return {"result": "ok", "details": pessoa}
    return {"result": "not_found", "details": None}
