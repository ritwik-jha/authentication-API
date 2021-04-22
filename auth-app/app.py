from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    passwd = db.Column(db.String, nullable=False)

    def __repr__(self):
        return ('User(id: {0}, username: {1}, email: {2})'.format(self.id, self.username, self.email))

@app.route('/signup/<username>/<email>/<passwd>')
def home(username,email,passwd):
    name_exist = User.query.filter_by(username=username).first()
    email_exist = User.query.filter_by(email=email).first()
    hashed_passwd = bcrypt.generate_password_hash(passwd).decode('utf-8')
    if name_exist or email_exist:
        return "Credentials already exist"
    else:
        user = User(username=username, email=email, passwd=hashed_passwd)
        db.session.add(user)
        db.session.commit()
        return "account created with username {} and email {}".format(username, email)


if __name__ == '__main__':
    app.run(port=80, debug=True)