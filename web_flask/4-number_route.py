#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def printTet(text):
    text = text.replace('_', ' ') if '_' in text else text
    return 'C ' + text

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ') if '_' in text else text
    return 'Python ' + text

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
