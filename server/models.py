from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

Base = declarative_base()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(32))
    email = db.Column(db.String(345), unique=True)
    password = db.Column(db.Text, nullable=False)

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.String(345), primary_key=True, default=get_uuid)
    quiz_id = db.Column(db.Integer)
    question = db.Column(db.Text(345))
    answers = db.Column(db.Text(690)) 
    correct_answer_index = db.Column(db.Integer)

class Quiz(db.Model):
    __tablename__ = 'quizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(345))

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Text(345))
    score = db.Column(db.Integer)
    quiz_id = db.Column(db.Integer)

    