import sys
from flask import g
from sqlalchemy import create_engine
from enum import Enum
from datetime import datetime

from app import app, db

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                       encoding='utf8', echo=False)


class Task(db.Model):
    __table__ = db.Table('task', db.metadata, autoload=True,
                         autoload_with=engine)

    def __repr__(self):
        return ('<User id: {0} username: {1} password: {2}>' +
                'mail: {3} tasks: {4} completed: {5}').format(
                self.user_id, self.username, self.password, self.u_mail,
                self.u_tasks, self.u_tasks_completed)


class User(db.Model):
    __table__ = db.Table('user', db.metadata, autoload=True,
                         autoload_with=engine)

    def __repr__(self):
        return ('<User id: {0} username: {1} password: {2}>' +
                'mail: {3} tasks: {4} completed: {5}').format(
                self.user_id, self.username, self.password, self.u_mail,
                self.u_tasks, self.u_tasks_completed)


class TodoStatus(Enum):
    TODO = 0
    INPROGRESS = 1
    ABANDON = 2
    DONE = 3

    def __str__(self):
        if self == TodoStatus.TODO:
            return "todo"
        elif self == TodoStatus.INPROGRESS:
            return "in-progress"
        elif self == TodoStatus.ABANDON:
            return "abandoned"
        elif self == TodoStatus.DONE:
            return "done"
        else:
            raise ValueError(
                    "enumeration invariant failed: value out of range")


class TodoItem:
    def __init__(self, task_id: int, title: str, begin: int, end: int,
                 description: str, status: int):
        self._t_id = int(task_id)
        self._title = str(title)
        self._begin = int(begin)
        self._end = int(end)
        self._desc = str(description)
        self._status = TodoStatus(status)


def get_db():
    if 'db' not in g:
        g.db = db.connect(host=app.config.DATABASE_HOST,
                          user=app.config.DATABASE_USER,
                          password=app.config.DATABASE_PASS,
                          db=app.config.DATABASE_NAME)
    try:
        print('Database setup completed', file=sys.stderr)
    except ValueError:
        print('Database already exists.', file=sys.stderr)
    finally:
        connection.close()
