'''
* Lets now retrieve the form data .
we will then use the data from the form to redirect user to user specific page.
we will modify our code as below. 
Our login.html remains the same i.e.

    {% extends "base2.html" %}

    {% block title %} Login Page {% endblock %}

    {% block content %} 
    <form action="#" method="POST">
    <p><label>Name</label></p> 
    <p><input type=text name="nm"/></p>
    <p><input type="submit" name="Login"/></p>>
    </form>
    {% endblock %}



whole flow:
user logins on: http://127.0.0.1:5000/login 
    ---> REDIRECTED TO USER PAGE WHEN INPUT 'DUNCAN' in text filed and  CLICK submit I.E.
        --> http://127.0.0.1:5000/Duncan


* We need to import request and url_for  libraries.

'''



from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route ("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form.get("nm")
        return redirect(url_for("user", usr=user))
    else:
        return  render_template ("login.html")

@app.route ("/<usr>")
def user(usr):
    return (f"<h1>{usr}</h1>")

if __name__ == "__main__":
    app.run(debug=True)



