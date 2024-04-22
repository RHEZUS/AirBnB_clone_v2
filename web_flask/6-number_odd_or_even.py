#!/usr/bin/python3

from flask import Flask
from flask import render_template

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

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    return render_template('5-number.html', num=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd(n):
    checked = 'even' if n%2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', number=n, checked=checked)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
