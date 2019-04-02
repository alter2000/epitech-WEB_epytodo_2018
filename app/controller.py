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
    return {'result': 'lol'}


def signin_user(req):
    return {'result': 'lol'}


def signout_user(req):
    return {'result': 'lol'}


def get_user(req):
    return {'result': 'lol'}


def get_user_tasks(req):
    return {'result': 'lol'}


def del_user_task(req):
    return {'result': 'lol'}


def add_user_task(req):
    return {'result': 'lol'}


def login_valid(req):
    return {'result': 'lol'}
