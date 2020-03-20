from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(80))
    location = db.Column(db.String(120))
    biography = db.Column(db.String(255))
    profile_pic = db.Column(db.String(80))
    date_created = db.Column(db.String(80))

    def __init__(self,firstName,lastName,gen,email,loc,bio,pic,date_joined):
        self.first_name = firstName
        self.last_name = lastName
        self.gender = gen
        self.email = email
        self.location = loc
        self.biography = bio
        self.profile_pic = pic
        self.date_created = date_joined

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
    
