'''
- Lets continue to render by passing some urguments that replaces content in html template.

'''

#render_template: This function helps to grab a html file and render it as our webpage.

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#To render and pass parameters 
#In html file we modified body to have jinja2:
#    <body>
#        <h1>Home Page</h1>
#        <p>{{content}}</p>
#    </body>
#Now the value of name we supply from frontend will accessing the url will be passed to replace content in html template.
#You can pass multiple parameters similar ways

@app.route("/<name>")
def home(name):
    return render_template("index.html", content = name) 


if __name__ == "__main__":
    app.run()