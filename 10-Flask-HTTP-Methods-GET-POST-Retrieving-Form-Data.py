'''
We will look at:
* HTTP Methods:
    > GET - Insecure way of getting data. When we type anything on the URL eg http://127.0.0.1:5000 anyone can see it, that will trigger a GET
    > POST - secure way of sending data. This is form data it wont be seen by users unless we are sending it to a database.

* Retrieving form data

LETs:
* Test POST
  STEP 1: - write below code

  STEP 2: - create login.html file as below so that we can render it:

    {% extends "base2.html" %}

    {% block title %} Login Page {% endblock %}

    {% block content %} 
    <form action="#" method="POST">
        <label>Name</label>
        <input type=text name="nm"/>
        <input type="submit" name="Login"/>
    </form>
    {% endblock %}


   STEP 3: When we run the page (http://127.0.0.1:5000/login) we see a '#' being added on our URL. This shows it is a POST i.e.
   http://127.0.0.1:5000/login#
   On the page we get text field for name and a submit button.
   when we input text and click on submit button, we see on terminal a post request being made:
   
   127.0.0.1 - - [10/Mar/2022 15:47:29] "POST /login HTTP/1.1" 200 -

   EVEN when we refresh the page we will still see the same.
'''



from flask import Flask, render_template

app = Flask(__name__)

@app.route ("/login", methods = ["POST","GET"]) #The default method is always GET.
def login():
    return  render_template ("login.html")

if __name__ == "__main__":
    app.run(debug=True)



