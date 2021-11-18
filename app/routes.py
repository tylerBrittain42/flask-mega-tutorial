from flask import render_template
from app import app

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
    # return 'Hello'