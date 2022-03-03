'''
- You can also write some python code in html template. This is nice.
- our example in html is now:

    <body>
        <h1>Home Page</h1>
        {% for x in range(10) %}
          {% if x % 2 == 1 %}
             <p>{{x}}</p>
          {% endif %}
        {% endfor %}
    </body>


This will print:

Home Page
1

3

5

7

9

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