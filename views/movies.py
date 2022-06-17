from flask_restx import Resource, Namespace
from decorators import auth_required, admin_required
from implemented import movie_service
from flask import request

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        args = request.args

        if 'director_id' in args:
            return movie_service.get_by_director_id(args['director_id'])

        if 'genre_id' in args:
            return movie_service.get_by_genre_id(args['genre_id'])

        if 'year' in args:
            return movie_service.get_by_year(args['year'])

        movies = movie_service.get_movies()
        return movies, 200

    @admin_required
    def post(self):
        data = request.get_json()
        movie_service.create(data)
        return "Фильм добавлен", 201


@movies_ns.route('/<id>')
class MovieView(Resource):
    @auth_required
    def get(self, id):
        movie = movie_service.get_movie(id)
        return movie, 200

    @admin_required
    def put(self, id):
        data = request.json
        movie_service.update(id, data)
        return 'Поля фильма изменены', 200

    @admin_required
    def delete(self, id):
        movie_service.delete(id)
        return 'Фильм удален', 200
