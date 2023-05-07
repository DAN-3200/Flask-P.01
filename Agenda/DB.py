from aplicacao import app, database, bcrypt
from aplicacao.models import Usuario

with app.app_context():
    database.create_all()

#with app.app_context():
#    database.drop_all()

#with app.app_context():
#     senha_crypto = bcrypt.generate_password_hash('123456')
#     user = Usuario(nome='admin', email='admin@gmail.com', senha=senha_crypto)
#     database.session.add(user)
#     database.session.commit()

#with app.app_context():
#     usuarios = Usuario.query.all()
#     for item in usuarios:
#         print(f'{item.nome}, {item.email}, {item.senha}, {item.id}')