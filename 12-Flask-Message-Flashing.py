'''
Ref:  askpython.com/python-modules/flask/flask-flash-method

* What does it mean to flash a message?
  It is always good for GUI applications to give feedback to the user for his actions.
  That is, for example, in Flask form, if the user leaves a field empty, it is appreciable to give him an error/info message 
  telling that the field is required.

*  In Flask, we have this flash method to do precisely that.

* How does Flask flash work?
The Flask flash method shows messages to the users.
With Flash, we can create a flash message in one Flask View and then show it in another View, called “next,” which usually is a template View.

* A typical example of Template View is:

@app.route('/template')
def blog():
    #codes...
    #codes...
    return render_template('template.html')

Hence, a Flask view creates a Flash message in one view and then passes it to the next view( along with the request), 
which displays the message to the user.

* The syntax for Flash:

    flash(message,category)

Here,

    message: The message to display
    category: An Optional parameter, which can be set to “error,” “info,” or “warning.”

* To extract the flash message from the session, where it is stored, and display it on the template, we use the get_flashed_messages() function.

get_flashed_messages(with_categories, category_filter)

Here:

    with_categories: An Optional Parameter tuple to mention the category(error/info/warning)
    category_filter: An Optional Parameter to filter and display only specific messages

A simple example showing the get_flashed_message() in Template file:

        {% with messages = get_flashed_messages() %}
        {% if messages %}
            {% for message in messages %}
                {{ message }}
            {% endfor %}
        {% endif %}
        {% endwith %}

* We will import flash library.

'''

from flask import Flask, render_template, request, redirect, flash, session


app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        password = request.form['password']
        if password == '123':
            
            #The below code will flash a message to the use when login is successful
            flash('Login successful')
            return render_template('success.html')
        else:
            return redirect('/form')


if __name__ == "__main__":
    app.run(debug=True)