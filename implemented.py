from dao.directors import DirectorsDAO
from dao.genres import GenresDAO
from dao.movies import MoviesDAO
from dao.users import UsersDAO
from service.directors import DirectorService
from service.genres import GenreService
from service.users import UserService
from service.movies import MovieService
from service.auth import AuthService
from setup_db import db


movies_dao = MoviesDAO(db.session)
movie_service = MovieService(movies_dao=movies_dao)


directors_dao = DirectorsDAO(db.session)
director_service = DirectorService(directors_dao=directors_dao)


genres_dao = GenresDAO(db.session)
genre_service = GenreService(genres_dao=genres_dao)


users_dao = UsersDAO(db.session)
user_service = UserService(users_dao=users_dao)


auth_service = AuthService(user_service=user_service)
