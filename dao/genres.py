from dao.model.genres import Genre, GenreSchema


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        genres = Genre.query.all()
        return GenreSchema(many=True).dump(genres)

    def get_genre(self, gid):
        genre = Genre.query.filter(Genre.id == gid).first()
        return GenreSchema().dump(genre)

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        self.session.close()

    def update(self, id, data):
        Genre.query.filter(Genre.id == id).update(GenreSchema().dump(data))
        self.session.commit()
        self.session.close()

    def delete(self, id):
        Genre.query.filter(Genre.id == id).delete()
        self.session.commit()
        self.session.close()