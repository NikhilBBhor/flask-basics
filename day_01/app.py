from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<H1>Hello World</H1>"


@app.route('/hello')
def hello():
    return "hello world"


@app.route('/great/<name>')
def great(name):
    return f"Hello {name}"


@app.route('/try_to_add/<num1>/<num2>') # parameters will be treated as string by default
def try_to_add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}" # result will be concatination


@app.route("/add/<int:num1>/<int:num2>") # both will be conder as integer, will get Not Found error when passed alphabets or special charaters
def add(num1, num2):  # if one of the parameter is missing, it will through Not Found error
    return f"{num1} + {num2} = {num1 + num2}"


@app.route("/handle_url_params") # /handle_url_params?name=Nikhil&greeting=Hello
def handle_params():
    greeting = request.args['greeting'] 
    name = request.args.get('name') # args[] and args.get(), both are same
    return f"{greeting}, {name}"


# if one of the parameter is missing, it will through BadRequestKeyError, eg./handle_url_params?name=Nikhil
# so doing following makes more sense
@app.route("/handle_params") # /handle_url_params?name=Nikhil&greeting=Hello
def handle_url_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args['greeting'] 
        name = request.args['name']
        return f"{greeting}, {name}"
    else:
        return "Some parameters are missing"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
