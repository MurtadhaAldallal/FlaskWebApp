from flask import render_template
from app import app #importing instance of Flask in app package
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Murtadha'}
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'I\'m not a fan of portland!'
        },
        {
        'author': {'username': 'Susan'},
        'body': 'Interstellar is the greatest movie!'
        }
    ]
    return render_template('index.html', title='Home' , user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)