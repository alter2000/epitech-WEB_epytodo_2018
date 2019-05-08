from flask import (abort,
                   render_template,
                   request,
                   jsonify,
                   make_response,
                   )
from flask_login import logout_user, login_required, current_user

from app import app, controller as con


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(app.config['ERR_OTHER']), 404)


@app.errorhandler(401)
def nologin(error):
    return make_response(jsonify(app.config['ERR_OTHER']), 401)


@app.errorhandler(400)
def wrong_request(error):
    return make_response(jsonify(app.config['ERR_OTHER']), 400)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def user_register():
    if request.method == 'GET':
        abort(401)
    if request.json is None or (
            'username' not in request.json or
            'password' not in request.json):
        return jsonify(app.config['ERR_OTHER'])
    return jsonify(con.add_user(request.json))


@app.route('/signin', methods=['POST', 'GET'])
def user_sign_in():
    if request.method == 'GET':
        abort(401)
    if request.json is None or (
            'username' not in request.json or
            'password' not in request.json):
        return jsonify(app.config['ERR_OTHER'])
    return jsonify(con.signin_user(request.json))


@app.route('/signout', methods=['POST', 'GET'])
@login_required
def user_sign_out():
    if request.method == 'GET':
        abort(401)
    logout_user()
    return jsonify(app.config['SIGNOUT_RES'])


@app.route('/<name>', methods=['GET'])
@login_required
def user_show_user(name):
    res = current_user.to_json()

    from sys import stderr
    print(res, file=stderr)

    return jsonify({'result': res})


@app.route('/<name>/task', methods=['GET'])
@login_required
def user_show_tasks(name):
    return jsonify(con.get_user_tasks(request.json))


@app.route('/<name>/task/<int:task>', methods=['GET'])
@login_required
def user_single(name, task):
    return jsonify(con.add_user_task(request.json))


@app.route('/<name>/task/add', methods=['POST'])
@login_required
def user_add(name):
    return jsonify(con.add_user(request.json))


@app.route('/<name>/task/del/<int:task>', methods=['POST'])
@login_required
def user_del(name, task):
    return jsonify(con.del_user_task(request.json))
