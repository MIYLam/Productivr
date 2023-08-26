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


@app.route("/home", methods = ["GET", "POST", "PUT"])
def home():
    
    if "username" not in session.keys():
        return redirect(url_for("login"))
    else:
        conn = sh.get_conn_object("data.db")
        user_id = sh.get_user_id_by_username(conn=conn, username=session["username"])
        print(user_id)
        g_ls = sh.get_user_groups(conn=conn, user_id=user_id).values.tolist()
        print(g_ls)
        
        if request.method == "GET":
            # display user tasks in each group
            tasks_by_group = {}
            group_names = []
            for g in g_ls:
                print(g)
                cid = sh.get_circlename_by_circle_id(conn=conn, circle_id=g)
                group_names.append(cid)
                tasks_by_group[g] = sh.get_user_tasks_by_circle(conn=conn, circle_id=g, user_id=user_id).to_dict('records')
            #    tasks_by_group[g] = sh.get_user_tasks(conn=conn, user_id=user_id, circle_id=cid)
            print(tasks_by_group)
            print(group_names)
            clist = zip(g_ls,group_names)
            
            return render_template("homepage.html", clist = clist, tasks = tasks_by_group)
          
        elif request.method == "POST":
            # create group
            if "Group Name" in request.form.keys():
                sh.add_circle(conn=conn, circlename=request.form["Group Name"], owner_id=user_id)            
            # join group
            elif True:
                circle_id: int = int(request.form["circle_id"])
                sh.user_join_circle(conn=conn, user_id=user_id, circle_id=circle_id)
                
            # display user tasks in each group
            tasks_by_group = {}
            group_names = []
            for g in g_ls:
                cid = sh.get_circlename_by_circle_id(conn=conn, circle_id=g)
                group_names.append(cid)
                #tasks_by_group[g] = sh.get_user_tasks(conn=conn, user_id=user_id, circle_id=cid)
            print(group_names)
            print(tasks_by_group)
            # return render_template("homepage.html", group_names = group_names)
            return redirect(url_for("home"))


@app.route("/group/<group_name>", methods = ["GET", "POST", "PUT", "DELETE"])
def group(group_name):

    if "username" not in session.keys():
        return redirect(url_for("login"))
    else:
        conn = sh.get_conn_object("data.db")
        user_id = sh.get_user_id_by_username(conn=conn, username=session["username"])
        user_list = sh.get_group_users(conn, group_name)
        print(user_list)
        if request.method == "GET":
            return render_template("group.html", users = user_list)
        elif request.method == "POST":
            # add a task
            if "task_description" in request.form.keys():
                sh.add_task(conn,user_id,group_name,request.form["task_name"],request.form["task_description"])
            else:
                sh.add_task(conn,user_id,group_name,request.form["task_name"],"")

            return redirect(f"{group_name}")
        elif request.method == "DELETE":
            # delete a task by id
            return render_template("group.html")
        else:
            # tick off a task
            return render_template("group.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)