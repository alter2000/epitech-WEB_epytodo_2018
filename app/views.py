from flask import (render_template,
                   request,
                   jsonify,
                   make_response)

from app import app, auth, controller as con


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify(app.config['ERR_OTHER']), 404)


@app.errorhandler(400)
def wrong_request(error):
    return make_response(jsonify(app.config['ERR_OTHER']), 400)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def user_register():
    if request.method == 'GET':
        return jsonify(app.config['ERR_OTHER'])
    if request.json is None or (
            'username' not in request.json or
            'password' not in request.json):
        return jsonify(app.config['ERR_OTHER'])
    return jsonify(con.add_user(request.json))


@app.route('/signin', methods=['POST', 'GET'])
def user_sign_in():
    if request.method == 'GET':
        return jsonify(app.config['ERR_OTHER'])
    if request.json is None or (
            'username' not in request.json or
            'password' not in request.json):
        return jsonify(app.config['ERR_OTHER'])
    return jsonify(con.signin_user(request.json))


@app.route('/signout', methods=['POST', 'GET'])
@auth.login_required
def user_sign_out():
    if request.method == 'GET':
        return jsonify(app.config['ERR_OTHER'])
    return jsonify(con.signout_user(request.json))


@app.route('/<name>', methods=['GET'])
@auth.login_required
def user_show_user(name):
    return jsonify(con.get_user(request.json))


@app.route('/<name>/task', methods=['GET'])
@auth.login_required
def user_show_tasks(name):
    return jsonify(con.get_user_tasks(request.json))


@app.route('/<name>/task/<int:task>', methods=['GET'])
@auth.login_required
def user_single(name, task):
    if request.method == 'GET':
        return jsonify(con.add_user_task(request.json))
    elif request.method == 'POST':
        return jsonify(con.login_valid(request.json))


@app.route('/<name>/task/add', methods=['POST'])
@auth.login_required
def user_add(name):
    return jsonify(con.add_user(request.json))


@app.route('/<name>/task/del/<int:task>', methods=['POST'])
@auth.login_required
def user_del(name, task):
    return jsonify(con.del_user_task(request.json))
