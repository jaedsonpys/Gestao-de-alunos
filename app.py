from flask import Flask, request
import json
from flask_restful import Resource, Api
from mysql import MySQL

app = Flask(__name__)
api = Api(app)

class Students(Resource):
    mysql = MySQL()

    def get(self):
        # obter alunos
        id = request.args.get('id')
        
        if id is None:
            response = self.mysql.get_student()
        else:
            response = self.mysql.get_student(id)
        
        if not response:
            response = {'error': True, 'message': 'Nenhum aluno encontrado'}

        return response

    def post(self):
        data = request.json
        print(data.keys())

        if len(data.keys()) < 6 or not data:
            return {'error': True, 'message': 'Algumas informações estão incompletas.'}

        result = self.mysql.set_student(data)
        if not result:
            return {'error': True, 'message': 'Entre em contato com o desenvolvedor para a resolução do problema'}

        return {'error': False, 'message': 'Aluno cadastrado com sucesso'}

    def put(self):
        id = request.args.get('id')
        data = request.json

        if not id:
            return {'error': True, 'message': 'Insira o ID do estudante'}

        if len(data.keys()) < 6 or not data:
            return {'error': True, 'message': 'Algumas informações estão incompletas.'}

        result = self.mysql.update_student(id, data)
        if not result:
            return {'error': True, 'message': 'Entre em contato com o desenvolvedor para a resolução do problema'}

        return {'error': False, 'message': 'Aluno atualizado com sucesso'}

    def delete(self):
        id = request.args.get('id')

        if not id:
            return {'error': True, 'message': 'Insira o ID do estudante'}

        result = self.mysql.delete_student(int(id))
        return {'error': False, 'message': f'Aluno de matrícula {id} foi deletado'}

api.add_resource(Students, '/students')

if __name__ == '__main__':
    app.run(debug=True)