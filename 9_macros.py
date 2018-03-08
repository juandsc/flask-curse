''' Example: how to use macros to call functions.'''
from flask import Flask
from flask import render_template as rt

app = Flask(__name__)

@app.route('/')
def index():
    my_title = 'Flask Curse'
    return rt('index_macro.html', title=my_title)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
