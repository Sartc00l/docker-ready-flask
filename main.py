from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
app.config['SQLACHEMY_TRACK-_MODIFICATIONS'] = False
db = SQLAlchemy(app)





class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(300),nullable=False)
    txt = db.Column(db.Text,nullable=False)


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
