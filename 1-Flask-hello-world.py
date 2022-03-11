'''

Ref Documentation: https://flask.palletsprojects.com/en/2.0.x/

* Flask is simple python micro web framework i.e. for developing web applications.
  Django is heavy due to the many built in apps it come along with.

* Flask is used to route web traffic through HTTP requests to specific functions in code base.

* Flask is WSGI Framework:
  WSGI (Web Server Gateway Interface) is an interface between web servers and web apps for python.

* comparisons:
  i- Databases: 
      Django: postgres, mysql, oracle
      Flask: mongoDB (Flask is preferred if you app doesnt need a database or needs nosql db)
    Therefore Django is a full stack framework while Flask falls in micro-framework.
  ii - Project size:
     Django: large projects 
     Flask: small projects

  iii - Project layout:
     Django: convectional
     Flask: Arbitary

  iv - Application type
    Django - full featured
    Flask - static

  v- RESTful API:
    Django: DRF
    Flask: RESTful, JWT

  vi - performance
    Django - performs less better than flask

  vii - TOP companies using them:
   Django: Instagram, pintrest, udemy
   Flask: Netflix, redit, lfyt
        

PRE-REQUISITES:
STEP 1: Lets create virtual enviromnent and activate it
        #python -m venv todo-flask
        #.\todo-flask\Scripts\activate

STEP 2: Install Flask:
        #pip install flask
        #pip list
        Package      Version
        ------------ -------
        Flask        2.0.3

* Now lets create a hello word application to test all is fine with our setup.
'''

from flask import Flask          #--> Import flask

app = Flask(__name__)            #--> Create an app instance from class Flask.

@app.route("/")                  #--> At the endpoint /
def hello():                     #--> Call method hello
        return "Hello World!"    #--> which returns "Hello world!"

if __name__ == "__main__":       #--> On running our python file "1-Flask-Hello_world.py"     
        app.run()                  #--> run the flask app

#This program displays 'Hello world!' on http://127.0.0.1:5000/


'''
*Debug mode*
For development purposes, we use something called as debug mode. 
When debug=True is set the server restarts as we add new code to our Flask Application. 
In order to set the debug mode do the following:
        -> Modify the line app.run() to app.run(debug=True).
        -> Stop the running server and restart it again.
You will see “debugger is active” which means that the debug mode has taken effect. 
Now you can go on and edit your file as much as you want, and the server will be restarted.

'''