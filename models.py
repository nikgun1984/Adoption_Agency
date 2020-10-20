from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):

    __tablename__ = "adopt_pets"

    id = db.Column(db.Integer,
                  primary_key = True,
                  autoincrement = True)

    name = db.Column(db.Text,
                    nullable = False)

    species = db.Column(db.Text,
                        nullable = False)

    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)

    def __repr__(self):
        return f"<Pet: (name:'{self.name}',species:'{self.species}', available:'{self.available}')>"


def connect_db(app):
    """Connect the database to our Flask app."""
    db.app = app
    db.init_app(app)