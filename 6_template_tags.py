''' Example of sending parameters to html template.'''
from flask import Flask
from flask import render_template as rt

app = Flask(__name__)
# Wrapper or decorator
@app.route('/user/<name>/')
@app.route('/user/<name>/<age>')
def index(name='No name', age='No age'):
    my_list = [1, 2, 3, 4]
    return rt('user.html', name=name, age=age, list=my_list)

if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
