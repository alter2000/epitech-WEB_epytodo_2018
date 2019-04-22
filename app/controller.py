from app.models import User, Task
from app import auth
from flask import g


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


@auth.verify_password
def login_valid(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return False
    g.user = user
    return True


def add_user(req):
    u = User()
    u.get(req)
    try:
        return u.add()
    except ValueError as e:
        return {'fname': 'add_user', 'err': e, 'data': req}


def signin_user(req):
    return {'fname': 'signin_user', 'data': req}


def signout_user(req):
    return {'fname': 'signout_user', 'data': req}


def get_user(req):
    return {'fname': 'get_user', 'data': req}


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
