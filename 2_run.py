''' Example of parameters for run methods'''
from flask import Flask

app = Flask(__name__)
# Wrapper or decorator
@app.route('/')
def index():
    return 'Hello World !!!'

if __name__ == '__main__':
    # Debug mode stay listening to deploy any change in the project
    app.run(debug=True, port=8000)
