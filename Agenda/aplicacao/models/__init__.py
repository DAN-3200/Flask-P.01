from aplicacao import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id):
    return Usuario.query.get(int(id))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    sobrenome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    numero = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

class Notas(database.Model):
    id_nota = database.Column(database.Integer, autoincrement=True, primary_key=True)
    id = database.Column(database.Integer, autoincrement=True)
    nota = database.Column(database.String, nullable=False)
