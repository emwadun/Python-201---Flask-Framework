'''
* Here we will learn about template inheritance so that you dont' have to repeat your code each time.
* You can re-use that base template. 
  We will create a base template that every other of your web pages can use.
* We will also add bootstrap on your website.
* In other words we will make decent website without frameworks like React or Angular etc.

STEP #1: We will create our base template known as base.html saved in templates folder example with below content:
NOTE: block...endblock are key words!

<!doctype html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title> 
    </head>
    <body>
        <h1>Tim's Website</h1>
        {% block content %}{% endblock %}
    </body>

</html>



STEP #2: Lets create a child template to use the base template as below. we will save as child.html:

{% extends "base.html" %}
{% block title%} Home Page {% endblock %}
{% block content %}
 <h1>Test 1</h1>
{% endblock %}


STEP #3: Write out python code as below.

STEO #4: On running the code and checking the page. below will be displayed:

Tim's Website
Test 1

'''

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("child.html") 


if __name__ == "__main__":
    app.run(debug=True)

#Now lets check on adding boostrap on our website.


