from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/uploads/'


# Secret Key
SECRET_KEY = 'C0mp3180$3cretkey'

user = 'oshea'
password = '@Xperia!123'
database = 'Comp3180_Project1'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://%s:%s@localhost/%s" % (user,password,database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views
