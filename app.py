from flask import Flask, render_template, request, session, redirect, url_for, send_file
import json
from typing import Dict

app = Flask(__name__,
            static_url_path="",
            static_folder="templates")

app.config['STATIC_FOLDER'] = "templates"
app.config["SECRET_KEY"] = "fmheiruwomhguweiomchpwnjslrfjio$%$#^@#$nfrwelfhuirqpbf"


@app.route("/", methods = ["GET", "POST"])
def login():
    session.clear()
    if "username" not in session.keys():
        if request.method == "GET":
            return render_template("index.html")
        elif request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            with open("users.json") as file: 
                users: Dict = json.load(file) 
            if username not in users.keys():
                return render_template("index.html") 
            else:
                if password == users[username]:
                    session["username"] = username
                    return redirect(url_for("home")) 
    else:
        return redirect(url_for("home"))


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if "username" not in session.keys():
        if request.method == "GET":
            return render_template("signup.html")
        else:
            with open("users.json") as file: 
                users: Dict = json.load(file) 
            username = request.form["username"]
            password = request.form["password"]
            if username not in users.keys():
                users[username] = password
                with open('data.json', 'w') as f:
                    json.dump(users, f)
                session["username"] = username
                return redirect(url_for(home))
            else:
                return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


app.route("/home", methods = ["GET", "POST", "PUT"])
def home():
    if "username" not in session.keys():
        return redirect(url_for("login"))
    else:
        if request.method == "GET":
            return render_template("home.html")
        elif request.method == "POST":
            # join a group
            return render_template("home.html")
        else:
            # create a group
            return render_template("home.html")


app.route("/group/<group_id>", methods = ["GET", "POST", "PUT", "DELETE"])
def group(group_id):
    if "username" not in session.keys():
        return redirect(url_for("login"))
    else:
        if request.method == "GET":
            return render_template("group.html")
        elif request.method == "POST":
            # add a task
            return render_template("group.html")
        elif request.method == "DELETE":
            # delete a task by id
            return render_template("group.html")
        else:
            # tick off a task
            return render_template("group.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)