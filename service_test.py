from service import *
from pony.orm import db_session, rollback

def test_insert():
    with db_session:
        response = insert("João Silva", "joao.silva@example.com", "123456789")
        rollback()
        assert response["result"] == "ok"
        assert "details" in response

def test_delete():
    with db_session:
        # Primeiro, insere uma pessoa para garantir que existe
        response_insert = insert("Maria Souza", "maria.souza@example.com", "987654321")
        pessoa_id = response_insert["details"]
        response_delete = delete(pessoa_id)
        rollback()
        assert response_delete["result"] == "ok"
        assert response_delete["details"] == 1
        # Tenta deletar uma pessoa que não existe
        response_delete_nonexistent = delete(99999)
        assert response_delete_nonexistent["result"] == "ok"
        assert response_delete_nonexistent["details"] == 0
