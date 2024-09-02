
from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blogs.db"
db = SQLAlchemy(app)

class blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    image = db.Column(db.String(200))
    post_date = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def index():
    blogposts = blog.query.all()
    return render_template("index.html", blogposts =blogposts )

@app.route('/<int:id>')
def post(id):
    blogpost = blog.query.get(id)
    return render_template("Post.html", blogpost =blogpost)


@app.route('/delete/<int:id>', methods = ['GET'])
def delete(id):
    delpost = blog.query.get(id)
    db.session.delete(delpost)
    db.session.commit()
    return redirect(url_for('index'))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run()