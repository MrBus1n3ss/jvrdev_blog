from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        "blog.html",
        blog_title='default',
        blog_data='some text'
    )

@app.route('/login')
def login():
    return render_template(
        "login.html"
    )