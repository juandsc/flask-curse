''' Example of managing routes'''
from flask import Flask
from flask import request

app = Flask(__name__)
# Wrapper or decorator
@app.route('/')
def index():
    return 'Hello World !!!'


@app.route('/sayhey')
def sayhey():
    return 'Say somebody!!!'


@app.route('/params')
def params():
    param1 = request.args.get('param1', 'Param not found')
    param2 = request.args.get('param2', 'Param not found')
    return 'First param: {}, second param: {}'.format(param1, param2)


if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
