import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_films")
def get_films():
    films = mongo.db.films.find()
    return render_template("films.html", films=films)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_movie_tvshow", methods=["GET", "POST"])
def add_movie_tvshow():
    if request.method == "POST":
        film = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "director": request.form.get("director"),
            "cast": request.form.get("cast"),
            "country": request.form.get("country"),
            "duration": request.form.get("duration"),
            "description": request.form.get("description"),
            "release_year": request.form.get("release_year"),
            "created_by": session["user"]
        }
        mongo.db.films.insert_one(film)
        flash("Show Successfully Added")
        return redirect(url_for("get_films"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_movie_tvshow.html", categories=categories)


@app.route("/edit_film/<film_id>", methods=["GET", "POST"])
def edit_film(film_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "director": request.form.get("director"),
            "cast": request.form.get("cast"),
            "country": request.form.get("country"),
            "duration": request.form.get("duration"),
            "description": request.form.get("description"),
            "release_year": request.form.get("release_year"),
            "created_by": session["user"]
        }
        mongo.db.films.update_one({"_id": ObjectId(film_id)}, {'$set': submit})
        flash("Show Successfully Updated")

    film = mongo.db.films.find_one({"_id": ObjectId(film_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_film.html", film=film, categories=categories)


@app.route("/delete_film/<film_id>")
def delete_film(film_id):
    mongo.db.films.delete_one({"_id": ObjectId(film_id)})
    flash("Show Successfully Deleted")
    return redirect(url_for("get_films"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)