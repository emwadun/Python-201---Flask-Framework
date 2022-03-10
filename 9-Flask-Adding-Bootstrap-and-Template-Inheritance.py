'''
* Bootstrap is a CSS framework.
* It is used to design and style in a fast way responsive websites.
* It makes the website looks nicer.
* Bootstrap is EASY!

REF: 
    - https://getbootstrap.com/

    
"Build fast, responsive sites with Bootstrap Quickly design and customize responsive mobile-first sites with Bootstrap, 
the world’s most popular front-end open source toolkit,  featuring Sass variables and mixins, responsive grid system, 
extensive prebuilt components, and powerful JavaScript plugins."

WE will
 * Style our base template using boostrap.
 * Style our base template using navbars from bootstrap.
 * use a child template and test our website.

REF: https://getbootstrap.com/docs/5.1/getting-started/introduction/

STEP #1: We will create our NEW base template known as base2.html saved in templates.
    NOTE: We will add the CSS styling and JS components to in head and body of the base template respectively.
    We need to copy them from:
    Ref: https://getbootstrap.com/docs/5.1/getting-started/introduction/


STEP #2: Lets create a child template to use the base template as below. we will save as child2.html:

{% extends "base.html" %}

STEP #3: Now lets add some navbars from bootstap. On above link search 'navbars'.
   NOTE: We will copy one from: https://getbootstrap.com/docs/5.1/components/navbar/
   and add in our body of our base template.

STEP #3: Write out python code as below.

STEO #4: On running the code and checking the page. below will be displayed:


'''

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("child2.html") 


if __name__ == "__main__":
    app.run(debug=True)




