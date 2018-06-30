# server.py
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    todos = []
    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=80)
