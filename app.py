from flask import Flask, render_template, request, session, redirect, url_for
import json
from typing import Dict
import sql_helper as sh

app = Flask(__name__, template_folder='templates', static_folder='static')

# app.config['STATIC_FOLDER'] = "static"
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

@app.route("/home", methods = ["GET", "POST", "PUT"])
def home():
    conn = sh.get_conn_object("data.db")

    if "username" not in session.keys():
        return redirect(url_for("login"))
    else:
        if request.method == "GET":

            # display user tasks in each group

            return render_template("homepage.html")
        elif request.method == "POST":
            # join a group
            user_id: int = sh.get_user_id_by_username(conn=conn, username=request.form["username"])
            circle_id: int = int(request.form["groupId"])
            sh.user_join_circle(conn=conn, user_id=user_id, circle_id=circle_id)

            # display user tasks in each group

            return render_template("homepage.html")
        else:
            # create a group
            user_id: int = sh.get_user_id_by_username(conn=conn, username=request.form["username"])
            # sh.add_circle(conn=conn, circlename=, owner_id=)
            return render_template("homepage.html")


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    conn = sh.get_conn_object("data.db")

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
                with open('users.json', 'w') as f:
                    json.dump(users, f, indent=2)
                session["username"] = username
                sh.add_user(conn=conn, username=username)
                return redirect(url_for("home"))
            else:
                return redirect(url_for("login"))
    else:
        return redirect(url_for("home"))


@app.route("/group/<group_id>", methods = ["GET", "POST", "PUT", "DELETE"])
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