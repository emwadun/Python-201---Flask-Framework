
'''
You can read more about __name__ = "__main__" here: 
https://www.freecodecamp.org/news/if-name-main-python-example/

'''
#redirect and url_for will help with redictions from specific functions ie redirect users to different pages.
#Each of the functions below are pages :)

from flask import Flask, redirect, url_for

#Lets create an instance 
app = Flask(__name__)

#lets create our pages
#Here we are saying if user access the root, the below text will be displayed.
@app.route("/")
def home():
    return "Hello! this is home page <h1> Hello Home page </h1>"

#Here on this page if user goes to /<type any name> it will display <Hello <that name typed>.
#For example we will use http://127.0.0.1:5000/duncan
#This will return "Hello Duncan!"
@app.route("/<name>")
def user(name):
    return (f"Hello {name}!")

#Here we want to redirect users who try to access admin to land them back to home page.
#In redirect and url_for functions we are using 'home' function name.
#ii.e. http://127.0.0.1:5000/admin --> They will be taken back to http://127.0.0.1:5000/
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()