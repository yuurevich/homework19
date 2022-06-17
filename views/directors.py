from flask_restx import Resource, Namespace
from decorators import auth_required, admin_required
from implemented import director_service
from flask import request

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all_directors()
        return directors, 200

    @admin_required
    def post(self):
        data = request.get_json()
        director_service.create(data)
        return "Режиссер добавлен", 201


@directors_ns.route('/<id>')
class DirectorsView(Resource):
    @auth_required
    def get(self, id):
        return director_service.get_director(id), 200

    @admin_required
    def put(self, id):
        data = request.json
        director_service.update(id, data)
        return 'Поля режиссера изменены', 200

    @admin_required
    def delete(self, id):
        director_service.delete(id)
        return 'Режиссер удален', 200