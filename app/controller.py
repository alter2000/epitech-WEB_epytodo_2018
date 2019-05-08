from app import app
from app.models import User, Task
from flask_login import current_user, login_user


def add_user(req):
    u = User()
    u.get(req)
    try:
        return u.add()
    except ValueError as e:
        return {'fname': 'add_user', 'err': e, 'data': req}


def signin_user(req):
    if current_user.is_authenticated:
        return app.config['SIGNIN_RES']
    user = User.query.filter_by(username=req['username']).first()
    if not user or not user.check_password(req['password']):
        return app.config['SIGNIN_ERR']
    login_user(user)
    return app.config['SIGNIN_RES']


def get_user_tasks(req):
    tl = Task.query.all()
    return {'result': {'tasks': [{t.task_id: {'title': str(t.title),
                                              'begin': str(t.begin),
                                              'end': str(t.end),
                                              'status': str(t.status)}}
                                 for t in tl]}}


def del_user_task(req):
    return {'fname': 'del_user_task', 'data': req}


def add_user_task(req):
    t = Task()
    t.get(req)
    try:
        return t.add()
    except ValueError as e:
        return {'fname': 'add_user_task', 'err': e, 'data': req}
