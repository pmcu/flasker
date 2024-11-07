from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a flask instance

app = Flask(__name__)

# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SECRET_KEY'] = "mysuperscretkey"

# Initialize the Data Base
db = SQLAlchemy(app)

# Create Model

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable= False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create String
    def __repr__(self):
        return '<Name %r>' % self.name

# Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    email = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email= form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User Added")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form = form,
                                            name = name,
                                            email = email,
                                            our_users=our_users)



# Create a route decorator
@app.route('/')

def index():
    first_name = "Jemmy"
    top_feeds =['spuds and butter','cowboy supper','fish and chips', 'scallions and champ',22]
#     return "<h1>Hello World dogs and donkeys</h1>"
    return render_template("index.html", 
first_name=first_name, 
top_feeds=top_feeds)

# User page
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
    
@app.route('/name', methods= ['GET','POST'])
def name(): 
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data 
        form.name.data = ''
        flash("Form submitted successfully")             
    
    return render_template('name.html',
    name = name,
    form = form)

    
if __name__ == '__main__':
    app.run(debug=True)