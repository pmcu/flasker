from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a flask instance

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysuperscretkey"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

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
    
    return render_template('name.html',
    name = name,
    form = form)

    
if __name__ == '__main__':
    app.run(debug=True)