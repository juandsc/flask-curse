''' Example of parameters in routes'''
from flask import Flask

app = Flask(__name__)
# Wrapper or decorator
@app.route('/')
def index():
    return 'Hello World !!!'


@app.route('/params/')
@app.route('/params/<name>/<int:num>')
def params(name='Default value', num='Defaul value'):
    return 'First param: {}, Second param: {}'.format(name, num)


if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
