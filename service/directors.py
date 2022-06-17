from dao.directors import DirectorsDAO


class DirectorService:

    def __init__(self, directors_dao: DirectorsDAO):
        self.directors_dao = directors_dao

    def get_all_directors(self):
        return self.directors_dao.get_all_directors()

    def get_director(self, did):
        return self.directors_dao.get_director(did)

    def create(self, data):
        self.directors_dao.create(data)

    def update(self, id, data):
        return self.directors_dao.update(id, data)

    def delete(self, id):
        return self.directors_dao.delete(id)