from flask_bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def overview():
    return render_template('overview.html', name='overview')

@app.route('/rabbits')
def rabbits():
    return render_template('rabbits.html', name='rabbits')

@app.route('/production')
def production():
    return render_template('production.html', name='production')

@app.route('/bypass')
def bypass():
    return render_template('bypass.html', name='bypass')