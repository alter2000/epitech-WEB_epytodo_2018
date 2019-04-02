from app import models as m


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'begin': '2019-01-01',
        'end': '2019-01-02',
        'status': m.TodoStatus.DONE,
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'begin': '2019-02-01',
        'end': '2019-02-02',
        'status': m.TodoStatus.TODO,
    }
]


def add_user(req):
    return {'fname': 'add_user'}


def signin_user(req):
    return {'fname': 'signin_user'}


def signout_user(req):
    return {'fname': 'signout_user'}


def get_user(req):
    return {'fname': 'get_user'}


def get_user_tasks(req):
    return {'fname': 'get_user_tasks'}


def del_user_task(req):
    return {'fname': 'del_user_task'}


def add_user_task(req):
    return {'fname': 'add_user_task'}


def login_valid(req):
    return {'fname': 'login_valid'}
