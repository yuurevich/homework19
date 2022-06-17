from dao.model.directors import Director, DirectorSchema

class DirectorsDAO():
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        directors = Director.query.all()
        return DirectorSchema(many=True).dump(directors)

    def get_director(self, did):
        director = Director.query.filter(Director.id == did).first()
        return DirectorSchema().dump(director)

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        self.session.close()

    def update(self, id, data):
        Director.query.filter(Director.id == id).update(DirectorSchema().dump(data))
        self.session.commit()
        self.session.close()

    def delete(self, id):
        Director.query.filter(Director.id == id).delete()
        self.session.commit()
        self.session.close()