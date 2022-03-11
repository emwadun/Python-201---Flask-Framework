'''
Python Flask CRUD Application. 

REF: 
- https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
- Relation between SQL and SQLAlchemy: https://www.compose.com/articles/using-postgresql-through-sqlalchemy/


WE need:
i - Flask,              ---> which we'll use to route web traffic through HTTP requests to specific functions in our code base
ii - SQLAlchemy,        ---> which we'll use to make the interaction between Python and our database smoother,
iii - Flask-SQLAlchemy, ---> which we'll use to make the interaction between Flask and SQLAlchemy smoother.

* We'll use the popular SQLite database, which comes bundled with the standard installation of Python. 
It is a file-based database, so we can store our data in a file on our file system, without needing to install a huge Relational Database Management System (RDBMS). 
We'll use SQLite through SQLAlchemy, which provides a higher level abstraction. 
This means that we could easily use a different database, such as PostgreSQL or MariaDB, and we wouldn't need to change our codebase. 
SQLAlchemy also allows us to do database level operations in a more Pythonic way.

Install them:
    #pip install flask sqlalchemy flask-sqlalchemy
    #pip list
    Package          Version
    ---------------- -------
    click            8.0.4
    colorama         0.4.4
    Flask            2.0.3  ---> *
    Flask-SQLAlchemy 2.5.1  ---> *
    greenlet         1.1.2
    itsdangerous     2.1.0
    Jinja2           3.0.3
    MarkupSafe       2.1.0
    pip              22.0.4
    setuptools       41.2.0
    SQLAlchemy       1.4.32  ---> *
    Werkzeug         2.0.3

NOTE: If we were creating this app without other exercise files, we would create:
1. A project folder named 'flask-crud-app' just to be clear or any relevant project name.
2. Then create this file naming it as bookmanager.py or relevant name and code as below

i.e. project structure
flask-crud-app/
    bookmanager.py
    templates/
        home.html

'''
#we import os python library to allow us to be able to access paths on our file system relative to our project directory.
import os

#We import Flask, render_template, request
from flask import Flask 
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

#we figure out where our project path is and set up a database file with its full path and the sqlite:/// prefix to tell SQLAlchemy which database engine we're using
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))


#nitialize a flask application, passing in Python's special __name__ variable to let Flask intelligently configure other parts of our application.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file #--> we tell our web application where our database is stored.

#we initialize a connection to the database and keep this in db variable. we'll use this to interact with our databse.
db = SQLAlchemy(app)



#In line 1 below, we create a new class which inherits from a basic database model, provided by SQLAlchemy. 
# This will also make SQLAlchemy create a table called book, which it will use to store our Book objects.

#In line 2 below, we create an attribute of our book called title. SQLAlchemy will use this as a column name in our book table. 
# We say that a title consists of a String of at most 80 characters, that we should never store two or more books with the same title (book titles should be unique), 
# that every book needs to have a title (the title isn't nullable), and that the title is the main way that we identify a specific book in our database (the title is the primary_key).

#In line 4-5 below, we define how to represent our book object as a string. This allows us to do things like print(book), and see meaningful output.

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr_(self):
        return "<Title: {}>".format(self.title)


#We use a Python decorator that Flask provides. This maps the main part of our application (/) to the home() function. 
#We'll see how routing works in more detail when we add more routes
#We then define a function that tell Flask to look for a template named home.html in 
# templates folder, process any logic it contains and return results to the user.
@app.route("/", methods=["GET", "POST"])
def home():
    # Here we check is someone submitted the form. 
    # Flask represents all form data as an ImmutableMultiDict which is just a fancy python dictionary.
    #Now, when we receive input from the user, we grab the "title" input from our form, and use it to initialize a new Book object. We save this new Book to a variable named boo
    #we then add the book to our datavase and commit our changes to persist them.
    if request.form:      
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
    
    #very time the user visits our web application, we want to get all of the current books out of the database and display them. 
    # SQLAlchemy makes it easy to load all of the books stored in our database into a Python variable. 
    # Here we retrieve all of the books just before the end of the home() function. we will update home.html template to render each of the books.
    books = Book.query.all()
    return render_template("home.html", books=books)

'''
One off activity, you need to Initialize the db. This is a one time step that needs to be run manually in python shell.
Run the following commands in a Python shell in your project directory in order to create our database and create the book table where we'll store our books. 

    >>> from bookmanager import db
    >>> db.create_all()
    >>> exit()

After that you can test Adding book from GUI! We are now done with the C part of CRUD.

'''

#We run our application behind an if guard. 
#This will ensure that we don't start up web servers if we ever import this script into another one (we'll only run the web server if we run this file explicitly).
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
