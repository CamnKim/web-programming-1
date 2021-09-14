from bottle import default_app, route, run, template

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/hello/<name>')
def hello_name(name):
    return 'hello ' + name + ' from /hello route'

@route('/goodbye/<name>')
def goodbye_html(name):
    return template("goodbye", name=name)

#application = default_app()
run(host="localhost", port=8080)
