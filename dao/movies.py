from dao.model.movies import Movie, MovieSchema


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = Movie.query.all()
        return MovieSchema(many=True).dump(movies), 200

    def get_movie(self, id):
        movie = Movie.query.filter(Movie.id == id).first()
        return MovieSchema().dump(movie)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def update(self, id, data):
        Movie.query.filter(Movie.id == id).update(MovieSchema().dump(data))
        self.session.commit()
        self.session.close()

    def delete(self, id):
        Movie.query.filter(Movie.id == id).delete()
        self.session.commit()
        self.session.close()

    def get_by_director_id(self, director_id):
        movies = Movie.query.filter(Movie.director_id == director_id).all()
        return MovieSchema(many=True).dump(movies), 200

    def  get_by_genre_id(self, genre_id):
        movies = Movie.query.filter(Movie.genre_id == genre_id).all()
        return MovieSchema(many=True).dump(movies), 200

    def get_by_year(self, year):
        movies = Movie.query.filter(Movie.year == year).all()
        return MovieSchema(many=True).dump(movies)