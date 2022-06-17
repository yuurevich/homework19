from flask_restx import Resource, Namespace
from decorators import auth_required, admin_required
from implemented import genre_service
from flask import request

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all_genres()
        return genres, 200

    @admin_required
    def post(self):
        data = request.get_json()
        genre_service.create(data)
        return "Жанр добавлен", 201


@genres_ns.route('/<id>')
class GenreView(Resource):
    @auth_required
    def get(self, id):
        return genre_service.get_genre(id), 200

    @admin_required
    def put(self, id):
        data = request.json
        genre_service.update(id, data)
        return 'Поля жанра изменены', 200

    @admin_required
    def delete(self, id):
        genre_service.delete(id)
        return 'Жанр удален', 200