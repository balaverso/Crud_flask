from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False, unique=True, index=True)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)


    def __init__(self, name, password):
        self.name = name
        self.password = generate_password_hash(password)
    
    def compare_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User: {self.username}"



class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __repr__(self):
        return self.name

class Moeda(db.Model):
    __tablename__ = 'moedas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=True, unique=True, index=True)
    var = db.Column(db.String(85), nullable=True)
    vol = db.Column(db.String(85), nullable=True)
    trades = db.relationship('Trade', backref='moeda')
    indicadores = db.relationship('Indicador', backref='moeda')
    def __repr__(self):
        return self.name

class Trade(db.Model):
    __tablename__ = 'trades'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    moeda_id = db.Column(db.Integer, db.ForeignKey('moedas.id'), nullable=False)
    
    def __repr__(self):
        return self.name

class Indicador(db.Model):
    __tablename__ = 'indicadores'

    id = db.Column(db.Integer, primary_key=True)
    min = db.Column(db.String(85), nullable=True, unique=True, index=True)
    max = db.Column(db.String(85), nullable=True, unique=True, index=True)
    abertura = db.Column(db.String(85), nullable=True, unique=True, index=True)
    ultimo = db.Column(db.String(85), nullable=True, unique=True, index=True)
    data = db.Column(db.Date, nullable=False)
    moeda_id = db.Column(db.Integer, db.ForeignKey('moedas.id'), nullable=False)
    
    def __repr__(self):
        return self.ultimo
