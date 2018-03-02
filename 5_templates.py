''' Example of templates renderization.'''
from flask import Flask
from flask import render_template as rt

app = Flask(__name__)
# To set another folder different to default 'templates'
# app = Flask(__name__, template_folder='some_folder')
# Wrapper or decorator
@app.route('/')
def index():
    return rt('index.html')

if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
