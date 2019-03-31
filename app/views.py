from flask import render_template, request, jsonify
import json

from app import app, controller as con


# index route, shows index.html view
@app.route('/', methods=('GET'))
def index():
    return render_template('index.html')


@app.route('/register', methods=('POST'))
def user_register(name):
    return render_template('index.html', username=name)


@app.route('/signin', methods=('POST'))
def user_sign_in(name):
    return render_template('index.html', username=name)


@app.route('/signout', methods=('POST'))
def user_sign_out(name):
    return render_template('index.html', username=name)


@app.route('/<name>', methods=('GET'))
def user_show_user(name):
    return render_template('index.html', username=name)


@app.route('/<name>/task', methods=('GET'))
def user_show_tasks(name):
    return render_template('index.html', username=name)


@app.route('/<name>/task/<int:task>', methods=('POST'))
def user_single(name, task):
    if request.method == 'GET':
        return jsonify({
                'id': task,
                'completed': json.loads(request.data).get('completed', 0)
                })
    elif request.method == 'POST':
        if con.login_valid(request.form['username'],
                           request.form['password']):
            return render_template('index.html', username=name)


@app.route('/<name>/task/add', methods=('POST'))
def user_add(name):
    data = json.loads(request.data)  # load JSON data from request
    return jsonify(data)


@app.route('/<name>/task/del/<int:task>', methods=('POST'))
def user_del(name, task):
    return jsonify({
                    'uid': name,
                    'tid': task,
                   })
