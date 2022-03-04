'''
- You can also write some python code in html template. This is nice.
- Our example in index3.html is now, we will print a list that will be passed from flask app:

<!doctype html>
<html>
    <head>
        <title>Home Page</title> 
    </head>
    <body>
        <h1>Home Page</h1>
        {% for i in content %}
             <p>{{i}}</p>
        {% endfor%}
    </body>

</html>


This will print:

Home Page
Duncan

Mike

Mel

Jas

'''

#render_template: This function helps to grab a html file and render it as our webpage.

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index3.html", content= ("Duncan", "Mike", "Mel", "Jas")) 


if __name__ == "__main__":
    app.run()


#lets try another example passing a list.