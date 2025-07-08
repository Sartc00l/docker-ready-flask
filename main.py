from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 
import sqlalchemy.exc
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


@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/pizdato")
def pizdato():
    return render_template("pizdato.html")


@app.route("/create",methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if not title:
            title == None

        post = Post(title=title,txt=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/pizdato')
        except sqlalchemy.exc.OperationalError as e: 
            return render_template('erors.html',data=e)
    else:
        return render_template("create.html")



if __name__ == "__main__":
    app.run(debug=True)
