from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

    mock_posts = [
        {
            'author': {'username':'Billy'},
            'body': 'I like trains'
        },
        {
            'author': {'username':'Steven'},
            'body': 'Boats are the superior transportation engine'
        }
    ]

    mock_user = {'username':'Tyler'}
    return render_template('index.html',title='home',user=mock_user, posts=mock_posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember me={form.remember_me.data}')
        return redirect(url_for('index'))    
    return render_template('login.html',title='Sign in', form=form)