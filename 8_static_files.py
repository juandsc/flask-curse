''' Example of templates with static files.'''
from flask import Flask
from flask import render_template as rt


app = Flask(__name__)
# Wrapper or decorator
@app.route('/')
def index():
    my_title = 'Flask Curse'
    return rt('index_static.html', title=my_title)


if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
