from flask import Flask, jsonify, request
from flasgger import Swagger

import json

app = Flask(__name__)
swagger = Swagger(app)

filmes = [
    {
    'id': 1,
    'titulo': 'A procura da felicidade',
    'genero': 'Drama',
    'nota': 5
    },
{
    'id': 2,
    'titulo': 'O pequenino',
    'genero': 'Comédia',
    'nota': 4
    },
{
    'id': 3,
    'titulo': 'Viagem ao centro da terra',
    'genero': 'Aventura',
    'nota': 3
    },
]


@app.route('/filmes', methods=['GET'])
def obter_filmes():
    """
       Obtém a lista de todos os filmes.
       ---
       responses:
         200:
           description: Uma lista de filmes.
       """
    return jsonify(filmes)

@app.route('/filmes/<int:id>', methods=['GET'])
def obter_filme_por_id(id):
    """
        Obtém um filme por ID.
        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID do filme.
        responses:
          200:
            description: Os detalhes do filme.
          404:
            description: Filme não encontrado.
        """
    for filme in filmes:
        if filme.get('id') == id:
            return jsonify(filme)

@app.route('/filmes/<int:id>', methods=['PUT'])
def editar_filme_por_id(id):
    """
        Atualiza um filme existente por ID.
        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID do filme a ser atualizado.
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                titulo:
                  type: string
                  description: Novo título do filme.
                genero:
                  type: string
                  description: Novo gênero do filme.
                nota:
                  type: integer
                  description: Nova nota do filme.
        responses:
          200:
            description: Detalhes do filme atualizado.
          404:
            description: Filme não encontrado.
        """
    filme_alterado = request.get_json()
    for indice,filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice])

@app.route('/filmes', methods=['POST'])
def incluir_novo_filme():
    """
       Adiciona um novo filme à lista.
       ---
       parameters:
         - name: body
           in: body
           required: true
           schema:
             type: object
             properties:
               titulo:
                 type: string
                 description: Título do novo filme.
               genero:
                 type: string
                 description: Gênero do novo filme.
               nota:
                 type: integer
                 description: Nota do novo filme.
       responses:
         201:
           description: Detalhes do novo filme adicionado.
       """
    novo_filme = request.get_json()
    filmes.append(novo_filme)
    return jsonify(filmes)

@app.route('/filmes/<int:id>', methods=['DELETE'])
def excluir_filme(id):
    """
        Exclui um filme por ID.
        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID do filme a ser excluído.
        responses:
          200:
            description: Lista de filmes após a exclusão.
          404:
            description: Filme não encontrado.
        """
    for indice, filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]
    return jsonify(filmes)

app.run(port=5000,host='localhost',debug=True)