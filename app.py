from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [{"id": 1, "nome": "Arthur"}]


@app.get("/")
def index():
    return jsonify({"mensagem": "API Flask rodando no Codespace"})


@app.get("/alunos")
def listar_alunos():
    return jsonify(alunos)


@app.post("/alunos")
def criar_aluno():
    dados = request.get_json(silent=True) or {}
    if "nome" not in dados:
        return jsonify({"erro": "campo 'nome' obrigatorio"}), 400
    aluno = {"id": len(alunos) + 1, "nome": dados["nome"]}
    alunos.append(aluno)
    return jsonify(aluno), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
