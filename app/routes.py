import importlib, sys
importlib.reload(sys)


from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ziv Tang'}
    return render_template('index.html', title='Home', user=user)

