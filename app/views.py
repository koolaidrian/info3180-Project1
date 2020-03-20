""" Additional Info is from info3180 lab 2 and 3. See for more infomation about Flask,
Jinja2, Werkzeug documentation """

import datetime
import os

from app import app
from app import db
from app.models import UserProfile
from .forms import ProfileForm
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename


""" Render the home page for the website """
@app.route('/')
def home():
    return render_template('home.html')



""" Render the about page for the website """
@app.route('/about/')
def about():
    return render_template('about.html', name = "Chanderpaul Campbell")


""" Render the profile page for the website """
@app.route('/profile' , methods = ['GET','POST'])
def profile():
    profileForm = ProfileForm()
    if request.method == "POST":
        if profileForm.validate_on_submit():
            profilepic = profileForm.profilePic.data
            filename = secure_filename(profilepic.filename)
            profilepic.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            firstName = profileForm.firstName.data
            lastName  = profileForm.lastName.data
            gen = profileForm.gender.data
            email = profileForm.email.data
            loc = profileForm.location.data
            bio = profileForm.biography.data
            date_joined = format_date_joined()

            user = UserProfile(firstName,lastName,gen,email,loc,bio,filename,date_joined)

            db.session.add(user)
            db.session.commit()

            

            flash('Profile was created successfully','success')
            return redirect(url_for('profiles'))
        else:
            flash(flash_errors(profileForm))
            
    return render_template('profile.html', form = profileForm)


""" Render for the profiles page for the website """
@app.route('/profiles')
def profiles():

    # users = db.session.query(UserProfile).all() for cloudy 9

    users = UserProfile.query.all()

    return render_template('profiles.html',users = users)
    
###             ###
# to be written   #
###             ###





""" Render for specific profile page for the website """

@app.route('/profile/<int:userid>') 
def myprofile(userid = 1):

    users = db.session.query(UserProfile).filter_by(id = userid) #for cloudy 9

    #users = UserProfile.query.all()

    return render_template('myprofile.html',users = users)
###             ###
# to be written   #
###             ###






def get_uploaded_images(filename):
    rootdir = os.getcwd()
    filenames = []
    print(rootdir)
    path = '/app/static/uploads'
    for subdir,dirs,files in os.walk(rootdir + path):
        for file in files:
            if file == ".gitkeep":
                continue;
            elif file == filename:
                return filename
               # filenames.append(file)
    #filenames.append("pic.jpg")

    return "default.png"
 
def format_date_joined():
    date_joined = datetime.datetime.now()
    return "Joined on " + date_joined.strftime("%B %m, %Y")

""" Flask Functions for application provided by sir """

def flash_errors(form):
    for field,errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'danger')


""" Send static text file .. not sure where thou """            
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


"""
    Add headers to both force lastes IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.

"""
@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge, chrome = 1'
    response.headers['Cache-Control'] = 'public, max-age = 0'
    return response


""" Custom 404 page """
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = "8080")

    







    

