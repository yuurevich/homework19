from service.users import UserService
from flask import abort, request
import calendar
import jwt
from datetime import datetime, timedelta
from constants import JWT_ALGORITHM, JWT_SECRET


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_user_by_username(username)

        if user is None:
            abort(404, 'User not found')

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                abort(400, 'ne sravnilos')

        data = {
            'username': user.username,
            'role': user.role
        }

        min30 = datetime.utcnow() + timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.utcnow() + timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            'refresh_token': refresh_token,
            'access_token': access_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
        username = data.get('username')

        return self.generate_tokens(username, None, is_refresh=True)