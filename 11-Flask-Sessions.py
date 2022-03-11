'''
SESSIONS:

* Lets improve out previous example using sessions to keep track of users. It is the best way than re-directing them to a /<user>

WHAT IS A SESSION? WHAT IS A COOKIE?

* Think of HTTP as a person(A) who has SHORT TERM MEMORY LOSS and forgets every person as soon as that person goes out of sight.
Now, to remember different persons, A takes a photo of that person and keeps it. 
Each Person's pic has an ID number. When that person comes again in sight, that person tells it's ID number to A and A finds their picture 
by ID number. And voila !!, A knows who is that person.

* Same is with HTTP. It is suffering from SHORT TERM MEMORY LOSS. 
It uses Sessions to record everything you did while using a website, and then, when you come again, 
it identifies you with the help of Cookies(Cookie is like a token). Picture is the Session here, and ID is the Cookie here.

* "Session" is the term used to refer to a user's time browsing a web site. 
It's meant to represent the time between their first arrival at a page in the site until the time they stop using the site. 
In practice, it's impossible to know when the user is done with the site. 
In most servers there's a timeout that automatically ends a session unless another page is requested by the same user.
The first time a user connects some kind of session ID is created (how it's done depends on the web server software and the type of authentication/login you're using on the site). Like cookies, this usually doesn't get sent in the URL anymore because it's a security problem. Instead it's stored along with a bunch of other stuff that collectively is also referred to as the session. Session variables are like cookies - they're name-value pairs sent along with a request for a page, and returned with the page from the server - but their names are defined in a web standard.

* Some session variables are passed as HTTP headers. 
They're passed back and forth behind the scenes of every page browse so they don't show up in the browser and tell everybody something that may be private.
Among them are the USER_AGENT, or type of browser requesting the page, the REFERRER or the page that linked to the page being requested, etc. 
Some web server software adds their own headers or transfer additional session data specific to the server software. But the standard ones are pretty well documented.

NOTE: session data persists a long as the browser page is not closed. If you need to persist the session data, you need to set up permenent storage of session data. it can span minutes, days etc.
if a user closes the browser, he/she can still get same session provided the minutes, days haven't elapsed.

* We need to import sessions  library

'''


from flask import Flask, redirect, render_template, request, url_for, session
from datetime import timedelta  #---> we need this to be able to setup permanent session data

app = Flask(__name__)
app.secret_key = 'hello'    # ----> Here we are creating a secret key. you can have any complicated string. Here we are using a simple to test.
app.permanent_session_lifetime = timedelta (minutes=5)   # ---> Here we are saying that we need to keep session data only for 5 minutes

@app.route ("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True   #----> Then here we are setting session to be permanent. The default value is False.
        user = request.form.get("nm")
        session["user"] = user       #----> Here we now set a session for this user we got from input.
        return redirect(url_for("user", usr=user))
    else:
        if "user" in session:
            return redirect(url_for("user")) #---> Here we are directing user to user page if we have session data
        return  render_template ("login.html")

@app.route ("/user")
def user():             # --> You can see we are now not passing username as a variable. This is nice.
    if "user" in session:
        user =  session["user"]
        return (f"<h1>{user}</h1>")
    else:
        return redirect(url_for("login"))   # --> This take user back to login page incase they passpass and coming straight to this page /user without going through /login


@app.route("/logout")
def logout():
    session.pop("user", None)       #--> This is how you remove the user info from session
    return redirect(url_for("login")) #--> Here we are re-directing the user back to login page

if __name__ == "__main__":
    app.run(debug=True)



