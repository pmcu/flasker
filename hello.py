from flask import Flask, render_template

# Create a flask instance

app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    first_name = "Jemmy"
    top_feeds =['spuds and butter','cowboy supper','fish and chips', 'scallions and champ',22]
#     return "<h1>Hello World dogs and donkeys</h1>"
    return render_template("index.html", 
first_name=first_name, 
top_feeds=top_feeds)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
    
    
    
if __name__ == '__main__':
    app.run(debug=True)