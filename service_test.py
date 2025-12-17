from service import *
from pony.orm import db_session, rollback

def test_insert():
    with db_session:
        response = insert("João Silva", "joao.silva@example.com", "123456789")
        rollback()
        assert response["result"] == "ok"
        assert "details" in response

