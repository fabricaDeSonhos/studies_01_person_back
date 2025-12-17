# app.py
from flask import Flask, request, jsonify
import service as svc  # <- usa o módulo estático que criamos antes

app = Flask(__name__)

API_BASE = "/api/pessoa"

from flask_cors import CORS
CORS(app, origins=['http://localhost:3000'])

# CREATE
@app.route(API_BASE, methods=["POST"])
def criar_pessoa():
    body = request.get_json(silent=True) or {}
    nome = body.get("nome")
    email = body.get("email")
    telefone = body.get("telefone", "")

    if not nome or not email:
        return jsonify({"result": "error", "message": "nome e email são obrigatórios"}), 400

    res = svc.insert(nome, email, telefone)  # retorna {"result":"ok","details":<id>}
    return jsonify({"result": res["result"], "id": res["details"]}), 201


# RETRIEVE ALL
@app.route(API_BASE, methods=["GET"])
def listar_pessoas():
    res = svc.retrieveAll()  # {"result":"ok","details":[...]}
    return jsonify(res), 200


# RETRIEVE BY ID
@app.route(f"{API_BASE}/<int:pessoa_id>", methods=["GET"])
def obter_pessoa(pessoa_id):
    res = svc.retrieveById(pessoa_id)  # {"result":"ok","details":{...}} ou {"result":"not_found","details":None}
    if res["result"] != "ok" or res["details"] is None:
        return jsonify({"result": "not_found"}), 404
    return jsonify(res), 200


# UPDATE (total/parcial)
@app.route(f"{API_BASE}/<int:pessoa_id>", methods=["PUT", "PATCH"])
def atualizar_pessoa(pessoa_id):
    body = request.get_json(silent=True) or {}
    nome = body.get("nome")
    email = body.get("email")
    telefone = body.get("telefone")

    # No service estático, o update só retorna 1/0 conforme o id existir
    res = svc.update(pessoa_id, nome=nome, email=email, telefone=telefone)  # {"result":"ok","details":1|0}

    if res["details"] == 0:
        return jsonify({"result": "not_found"}), 404

    return jsonify({"result": "ok", "updated": 1}), 200


# DELETE
@app.route(f"{API_BASE}/<int:pessoa_id>", methods=["DELETE"])
def apagar_pessoa(pessoa_id):
    res = svc.delete(pessoa_id)  # {"result":"ok","details":1|0}

    if res["details"] == 0:
        return jsonify({"result": "not_found"}), 404

    return jsonify({"result": "ok", "deleted": 1}), 200


if __name__ == "__main__":
    app.run(debug=True)
