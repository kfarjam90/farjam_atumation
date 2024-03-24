from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return 'heloo'

@app.route('/hello', methods=["GET","POST"])
def hello():
    if request.method == 'GET':
        return 'get request'
    elif request.method == 'POST':
        return 'post request'
    else:
        return 'not happend!!'

@app.route('/greeting/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2):
    return f'{number1} +{number2} = {number1} + {number2}'


@app.route('/handle_url_params')
def handle_parmas():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'have a problem'


if __name__ == '__main__':
    app.run(debug=True)