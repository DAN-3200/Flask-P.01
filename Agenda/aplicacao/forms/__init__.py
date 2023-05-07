from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, email, equal_to

class Form_Login(FlaskForm):
    email = StringField('e-mail', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    lembrar = BooleanField('Lembrar-se')
    SingUp = SubmitField('Entrar')
    SingIn =SubmitField('Cadastrar')

class Form_Cadastro(FlaskForm):
    nome = StringField('Nome de Usuário', validators=[DataRequired(), length(5, 12)])
    sobrenome = StringField('Sobrenome do Usuário', validators=[DataRequired(), length(5, 11)])
    email = StringField('e-mail', validators=[DataRequired(), email()])
    numero = StringField('Celular', validators=[DataRequired(),length(11,11)])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])
    criar = SubmitField('Criar')

class Notas(FlaskForm):
    titulo = StringField('Titulo')
    nota = StringField('Digite...')
