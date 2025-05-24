from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# with app.app_context():
#     db.create_all()

# @app.route('/')
# def index():
#     users = User.query.all()
#     return render_template('index.html', users=users)

# @app.route('/add', methods=['POST'])
# def add_user():
#     name = request.form['name']
#     email = request.form['email']
#     user = User(name=name, email=email)
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/update', methods=['POST'])
# def update_user():
#     user_id = request.form['id']
#     name = request.form['name']
#     email = request.form['email']
#     user = User.query.get(user_id)
#     if user:
#         user.name = name
#         user.email = email
#         db.session.commit()
#     return redirect(url_for('index'))

# @app.route('/delete/<int:id>')
# def delete_user(id):
#     user = User.query.get(id)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#     return redirect(url_for('index'))



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/map')
def map_view():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)