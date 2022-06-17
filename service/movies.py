from dao.movies import MoviesDAO


class MovieService:
    def __init__(self, movies_dao: MoviesDAO):
        self.movies_dao = movies_dao

    def get_movies(self):
        return self.movies_dao.get_all_movies()

    def get_movie(self, id):
        return self.movies_dao.get_movie(id)

    def create(self, data):
        self.movies_dao.create(data)

    def update(self, id, data):
        return self.movies_dao.update(id, data)

    def delete(self, id):
        return self.movies_dao.delete(id)

    def get_by_genre_id(self, genre_id):
        return self.movies_dao.get_by_genre_id(genre_id)

    def get_by_director_id(self, director_id):
        return self.movies_dao.get_by_director_id(director_id)

    def get_by_year(self, year):
        return self.movies_dao.get_by_year(year)