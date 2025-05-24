from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/map')
def map_view():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)