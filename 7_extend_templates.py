''' Example of template extends.'''
from flask import Flask
from flask import render_template as rt


app = Flask(__name__)
# Wrapper or decorator
@app.route('/user/<name>/')
def user(name='No name'):
    my_name = name
    return rt('index_extend.html', name=my_name)


@app.route('/client')
def client():
    my_list_name = ['juan', 'ana', 'rosa']
    return rt('client.html', list_name=my_list_name)


if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
