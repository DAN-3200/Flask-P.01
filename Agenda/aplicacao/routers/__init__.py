from aplicacao import app, database, bcrypt
from flask import redirect, render_template, url_for, flash
from aplicacao.forms import Form_Login, Form_Cadastro
from aplicacao.models import Usuario
from flask_login import login_user, logout_user, login_required


@app.route('/', methods= ['GET', 'POST'])
def Login():
    form = Form_Login()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user, remember=form.lembrar.data)
            flash(f'Login feito com sucesso para o user: {form.email.data}', 'alert alert-success')
            return redirect('home')
        else:
            flash(f'Usuário ou senha inválidos', 'alert alert-danger')
    return render_template('login.html', form=form)
def btn_cadastro():
    form = Form_Login()
    if form.SingIn.data:
        pass
        return redirect('cadastro')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = Form_Cadastro()
    if form.validate_on_submit():
        senha_crypto = bcrypt.generate_password_hash(form.senha.data)
        try:
            user = Usuario(nome=form.nome.data,sobrenome=form.sobrenome.data, email=form.email.data, senha=senha_crypto
                           , numero=form.numero.data)
            database.session.add(user)
            database.session.commit()
            flash(f'Usuário cadastrado com sucesso', 'alert alert-success')
            return redirect(url_for('home'))
        except:
            flash(f'Não foi possível cadastrar usuário', 'alert alert-danger')
    return render_template('register.html', form=form)

@app.route('/home')
def home():
    return render_template('home.html')
