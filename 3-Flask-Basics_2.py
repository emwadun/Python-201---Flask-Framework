'''
Lets see how we can can redirect by passing variables.
'''

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is home page <h1> Hello Home page </h1>"

@app.route("/<name>")
def user(name):
    return (f"Hello {name}!")

#Here is how to re-direct lets say to another page/function that needs a parameter.
#here user on accessing /admin will be redirected to user page with his/her name i.e.
#on accessing http://127.0.0.1:5000/admin ----will be directed to --> http://127.0.0.1:5000/owino
#screen will show message: Hello owino!

@app.route("/admin")
def admin():
    return redirect(url_for("user", name = "owino"))

if __name__ == "__main__":
    app.run()