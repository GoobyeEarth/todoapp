# server.py
from flask import Flask
from flask import render_template
from flask import request

from datetime import datetime

import db

app = Flask(__name__)


@app.route('/')
def index():
    todos = []
    return render_template('index.html', todos=todos)


@app.route('/register', methods=['POST'])
def register():
    db.todo.insert().execute(contents=request.form['contents'], created_at=datetime.now())

    todos = db.todo.select().execute().fetchall()
    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=80)
