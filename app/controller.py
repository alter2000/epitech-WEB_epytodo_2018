from functools import wraps
from flask import g, request, abort

from app import app, users
from app.models import User, Task

# testing shiz
from app.models import TodoStatus
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'begin': '2019-01-01',
        'end': '2019-01-02',
        'status': TodoStatus.DONE,
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'begin': '2019-02-01',
        'end': '2019-02-02',
        'status': TodoStatus.TODO,
    }
]


def login_required(f):
    @wraps(f)
    def decf(*args, **kwargs):
        name = getattr(kwargs, 'name', None)
        if not name or name not in (u.username for u in users):
            abort(401)
        return f(*args, **kwargs)
    return decf


def add_user(req):
    u = User()
    u.get(req)
    try:
        return u.add()
    except ValueError as e:
        return {'fname': 'add_user', 'err': e, 'data': req}


def signin_user(req):
    user = User.query.filter_by(username=req['username']).first()
    if not user or not user.check_password(req['password']):
        return app.config['SIGNIN_ERR']
    if user not in users:
        users.append(user)
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
