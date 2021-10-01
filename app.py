from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import os
import pymysql
from flask_mail import Mail, Message

app = Flask(__name__)
Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/User'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    admin = db.Column(db.String(20))

class User_id(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(15), unique=True)
    used = db.Column(db.String(15))
    admin = db.Column(db.String(15))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Recordar sesion')

class RegisterForm(FlaskForm):
    email = StringField('Correo', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    username = StringField('Usuario', validators=[InputRequired(), Length(min=4, max=15)])
    user_id = StringField('Id personal', validators=[InputRequired(), Length(min=3, max=3)])
    password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max=80)])

class CreateID(FlaskForm):
    user_id = StringField('ID de usuario', validators=[InputRequired(), Length(min=3, max=3)])
    admin = StringField('Admin?', validators=[InputRequired(), Length(min=3, max=3)])

class recover(FlaskForm):
    email = StringField('Correo', validators=[InputRequired(), Email(message='Correo Invalido'), Length(max=50)])
    user_id = StringField('ID de usuario', validators=[InputRequired(), Length(min=3, max=3)])
    new_password = PasswordField('Contraseña', validators=[InputRequired(), Length(min=6, max=80)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                if (user.admin == 'yes'):
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('dashboard'))
        return render_template('login.html', predict_content='Contraseña o usuario incorrecto', form=form)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_paswrd = generate_password_hash(form.password.data, method='sha256')
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        user_id = User_id.query.filter_by(user_id=form.user_id.data).first()
        if (user):
            return render_template('signup.html', form=form, user_in_use='El Usuario Ingresado Ya existe')
        if(email):
            return render_template('signup.html', form=form, email_in_use='El Correo Ingresado Ye exite')
        
        if(user_id):
            if (user_id.used != 'used'):
                unique_id = User_id(user_id=form.user_id.data, used='used')
            else:
                return render_template('signup.html', form=form, wrong_id='Este ID de trabajador ya esta en uso, verifique su ID')
        else:
            return render_template('signup.html', form=form, wrong_id='Id de trabajador incorrecto comuniquese con el administrador')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_paswrd, admin=user_id.admin)
        update_user = User_id.query.filter_by(user_id=form.user_id.data).update({'used':'used'})

        db.session.add(new_user)
        db.session.commit()
        return render_template('signup.html', form=form, complete='Registro Completado')
    return render_template('signup.html', form=form)

@app.route('/recover', methods=['GET', 'POST'])
def recover_pwd():
    form = recover()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        user_id = User_id.query.filter_by(user_id=form.user_id.data).first()
        print(user_id)
        if (user == None):
            return render_template('recover_account.html', form=form, wrong_email='El Correo No Existe')
        if (user_id == None or user_id.user_id != form.user_id.data):
            return render_template('recover_account.html', form=form, wrong_id='El ID de usuario no existe')
        hashed_paswrd = generate_password_hash(form.new_password.data, method='sha256')
        user = User.query.filter_by(email=form.email.data).update({'password': hashed_paswrd})
        db.session.commit()
        return render_template('recover_account.html', form=form, complete='Contraseña Actualizada')


    return render_template('recover_account.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = CreateID()
    if form.validate_on_submit():
        user_id = User_id.query.filter_by(user_id=form.user_id.data).first()
        if (user_id):
            return render_template('admin.html', form=form, wrong_id='EL ID ya existe')
        else:
            new_user = User_id(user_id=form.user_id.data, used='false', admin=form.admin.data)
            db.session.add(new_user)
            db.session.commit()
            return render_template('admin.html', form=form, complete='ID Creado Correctamente')
    return render_template('admin.html', form=form)

@app.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
