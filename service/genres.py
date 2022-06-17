from dao.genres import GenresDAO


class GenreService:

    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao

    def get_all_genres(self):
        return self.genres_dao.get_all_genres()

    def get_genre(self, gid):
        return self.genres_dao.get_genre(gid)

    def create(self, data):
        self.genres_dao.create(data)

    def update(self, id, data):
        return self.genres_dao.update(id, data)

    def delete(self, id):
        return self.genres_dao.delete(id)