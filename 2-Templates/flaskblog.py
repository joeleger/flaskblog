from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Joseph Leger',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Kristin Alter Leger',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return  render_template("about.html", title = 'About')


if __name__ == '__main__':
    app.run(debug=True)
