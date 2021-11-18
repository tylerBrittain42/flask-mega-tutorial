from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    mock_user = {'username':'Tyler'}
    return render_template('index.html',title='home',user=mock_user)
    # return 'Hello'