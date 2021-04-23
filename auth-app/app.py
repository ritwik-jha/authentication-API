from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dlskfjlkjdalskfjklajdflk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    passwd = db.Column(db.String, nullable=False)

    def __repr__(self):
        return ('User(id: {0}, username: {1}, email: {2})'.format(self.id, self.username, self.email))

@app.route('/signup')
def signuponly():
    return 'use proper route: <br> http://ip:80/signup/username/email/password'

@app.route('/login')
def loginonly():
    return 'use proper route: <br> http://ip:80/login/email/password'
    
@app.route('/signup/<username>/<email>/<passwd>')
def signup(username,email,passwd):
    name_exist = User.query.filter_by(username=username).first()
    email_exist = User.query.filter_by(email=email).first()
    hashed_passwd = bcrypt.generate_password_hash(passwd).decode('utf-8')
    if name_exist or email_exist:
        return "User already exist"
    else:
        user = User(username=username, email=email, passwd=hashed_passwd)
        db.session.add(user)
        db.session.commit()
        return "account created with username {} and email {}".format(username, email)

@app.route('/login/<email>/<password>')
def login(email,password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.passwd, password):
        login_user(user, remember=True)
        return 'Login for user {} is successful ;)'.format(user.username)
    else:
        return 'No such user !!! please check your credentials'

@app.route('/currentuser')
def currentuser():
    if current_user.is_authenticated:
        current_user_id = current_user.get_id()
        if User.query.filter_by(id=current_user_id).first():
            return 'user ' + str(User.query.filter_by(id=current_user_id).first().username) + ' is logged in'
    else:
        return 'No user logged in !! Login to continue '

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        if User.query.filter_by(id=current_user.get_id()).first():
            current_user_name =  User.query.filter_by(id=current_user.get_id()).first().username
            logout_user()
            return 'successfully logged out user {}'.format(current_user_name)
    else:
        return 'No user logged in'

@app.route('/dump')
def dump():
    rows = []
    for i in User.query.all():
        row = []
        row.append(i.id)
        row.append(i.username)
        row.append(i.email)
        row.append(i.passwd)
        rows.append(row)
    
    fields = ['id','username','email','password']
    filename = 'backup.csv'
    with open(filename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)
    
    return 'Backup done'



@app.route('/showbackup')
def showbackup():
    file = open('/root/authentication-API/auth-app/backup.csv', 'r')
    op = []
    for i in file:
         op.append(i.strip())
         op.append('<br>')
    file.close()
    string = ''
    final = string.join(op)  
    return final




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
