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

def test_update():
    with db_session:
        # Insere uma pessoa para atualizar
        response_insert = insert("Carlos Lima", "carlos.lima@example.com", "555555555")
        pessoa_id = response_insert["details"]
        response_update = update(pessoa_id, nome="Carlos L. Silva")
        rollback()
        assert response_update["result"] == "ok"
        assert response_update["details"] == "ok"
        # Tenta atualizar uma pessoa que não existe
        response_update_nonexistent = update(99999, nome="Nome Inexistente")
        assert response_update_nonexistent["result"] == "error"
        assert "Pessoa not found" in response_update_nonexistent["details"]

def test_retrieveAll():
    with db_session:
        # Insere algumas pessoas para garantir que há dados
        insert("Ana Paula", "ana.paula@example.com", "111111111")
        insert("Bruno Costa", "bruno.costa@example.com", "222222222")
        pessoas = retrieveAll()
        rollback()
        assert pessoas["result"] == "ok"
        for p in pessoas["details"]:
            assert "id" in p
            assert "nome" in p
            assert "email" in p
            assert "telefone" in p
            assert p["nome"] == "Ana Paula" or p["nome"] == "Bruno Costa"
            # print(f" content: {p}")
        
