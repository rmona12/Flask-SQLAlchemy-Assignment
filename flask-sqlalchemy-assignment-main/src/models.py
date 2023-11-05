# TODO - Create SQLAlchemy DB and Movie model
from src.models import Movie
from app import db

class Movie(db.Model):
    tablename = 'movie'
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)