from bottle import route, run, template, get, post, request

#http://localhost:8080 <route>
message= ""

@route("/")
def get_index():
    return ("Hello!")
    

@route("/hello")
def get_index():
    return ("Hello!")

@get("/hello/<name>")
def get_name(name="world"):
    return template("hello.tpl", name="Bob", extra="Happy birthday!")

@get("/greet")
@get("/greet/<name>")
def get_name(name="world"):
    return template("hello.tpl", name="Bob", extra=None)

@get("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template("greetings", names=names)

@get("/login")
def get_login():
    return template("login", message="")

@post("/login")
def post_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if password != "password":
        return template("login", message="bad password")
    return template("hello.tpl", name=username, extra="Happy birthday!")



run(host="localhost", port=8080)