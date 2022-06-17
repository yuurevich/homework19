import base64
import hashlib
import hmac
from dao.users import UsersDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, users_dao: UsersDAO):
        self.users_dao = users_dao

    def get_all_users(self):
        return self.users_dao.get_all_users()

    def get_user(self, id):
        return self.users_dao.get_user(id)

    def create(self, data):
        data['password'] = self.generate_password(data['password'])
        return self.users_dao.create(data)

    def update(self, id, data):
        data['password'] = self.generate_password(data['password'])
        return self.users_dao.update(id, data)

    def delete(self, id):
        return self.users_dao.delete(id)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
            )
        return base64.b64encode(hash_digest)

    def get_user_by_username(self, username):
        return self.users_dao.get_user_by_username(username)

    def compare_password(self, password_hash, other_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)