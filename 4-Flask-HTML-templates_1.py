'''
- we will use render_template function.
- This function helps to grab a html file and render it as our webpage.

step 1: Create a folder named 'templates' it must be in same directory as your project.
step 2: create html file(s) and save in it. lets create one named index.html
step 3: lets render it as below


'''

#render_template: This function helps to grab a html file and render it as our webpage.

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

#Now this will display the page we created in html. it will render it.
#This is how we render html templates.
@app.route("/")
def home():
    return render_template("index.html") 



if __name__ == "__main__":
    app.run()