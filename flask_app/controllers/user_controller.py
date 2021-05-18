from flask import render_template,redirect,request,session,flash

from flask_app import app
from flask_app.models.user import User

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


# Read One
@app.route("/users/<int:user_id>")
def show_user(user_id):
    this_user = User.get_one_user( {"id": user_id } )

    return render_template("result.html", user = this_user)


# Create
@app.route("/users/create", methods = ["POST"])
def add_user():
    # Validate post data
    # If invalid, redirect tot he form and tell theuser what they didn wrong
    if not User.validate_user(request.form):
        return render_template ("index.html")

    # if the data is valid, create the user
    user_id = User.add_user(request.form) 

    return redirect(f"/users/{user_id}")
