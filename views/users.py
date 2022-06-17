from flask_restx import Resource, Namespace
from decorators import admin_required
from implemented import user_service
from flask import request

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        return user_service.get_all_users()

    def post(self):
         return user_service.create(request.json)


@users_ns.route('/<id>')
class UserView(Resource):
    def get(self, id):
        return user_service.get_user(id), 200

    @admin_required
    def put(self, id):
        data = request.json
        user_service.update(id, data)
        return 'Поля пользователя изменены', 200

    @admin_required
    def delete(self, id):
        user_service.delete(id)
        return 'Пользователь удален', 200


