from dao.model.users import User, UserSchema


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        users = User.query.all()
        return UserSchema(many=True).dump(users)

    def get_user(self, id):
        user = User.query.filter(User.id == id).first()
        return UserSchema().dump(user)

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def update(self, id, data):
        User.query.filter(User.id == id).update(UserSchema().dump(data))
        self.session.commit()
        self.session.close()

    def delete(self, id):
        User.query.filter(User.id == id).delete()
        self.session.commit()
        self.session.close()

    def get_user_by_username(self, username):
        user = User.query.filter(User.username == username).first()
        return user