from enum import Enum
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from app import app, db

# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
#                        encoding='utf8', echo=False)


class TodoStatus(Enum):
    TODO = 0
    INPROGRESS = 1
    ABANDON = 2
    DONE = 3

    def __int__(self):
        if self == TodoStatus.TODO:
            return (self.TODO)
        elif self == TodoStatus.INPROGRESS:
            return (self.INPROGRESS)
        elif self == TodoStatus.ABANDON:
            return (self.ABANDON)
        elif self == TodoStatus.DONE:
            return (self.DONE)
        else:
            raise ValueError("enumeration failed: value out of range")

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
            raise ValueError("enumeration failed: value out of range")


class Task(db.Model):
    __table__ = db.Model.metadata.tables['task']

    def __repr__(self):
        return ('<Task(id="{0}", title="{1}", begin="{2}", ' +
                'end="{3}", desc="{4}", status="{5}")>').format(
                self.task_id, self.title, self.begin, self.end,
                self.t_description, self.status)

    def to_json(self):
        return {'task_id': self.task_id,
                'title': self.title,
                'begin': self.begin,
                'end': self.end,
                't_description': self.description,
                'status': self.status}

    def get(self, req):
        self.title = req.get('title')
        self.begin = req.get('begin')
        self.end = req.get('end')
        self.t_description = req.get('t_description')
        self.status = req.get('status')

    def add(self):
        if self.title is None:
            raise ValueError("task needs title")
        if self.end is None:
            raise ValueError("task needs end time")
        if self.status is None:
            self.status = TodoStatus.TODO

        db.session.add(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return app.config['ERR_OTHER']
        finally:
            return app.config['TASK_ID_ADD_RES']


class User(db.Model):
    __table__ = db.Model.metadata.tables['user']

    def __repr__(self):
        return ('<User(id={0}, name={1}, pass={2}, ' +
                'mail={3}, tasks={4}, compl={5})>').format(
                self.user_id, self.username, self.password[:12],
                self.u_mail, self.u_tasks, self.u_tasks_completed)

    def to_json(self):
        return {'user_id': self.user_id,
                'username': self.username,
                'password': self.password,
                'u_mail': self.u_mail,
                'u_tasks': self.u_tasks,
                'u_tasks_completed': self.u_tasks_completed}

    def get(self, req):
        self.username = req.get('username')
        self.password = generate_password_hash(req.get('password'))
        self.u_mail = req.get('u_mail')
        self.u_tasks = req.get('u_tasks')
        self.u_tasks_completed = req.get('u_tasks_completed')

    def add(self):
        if self.username is None:
            raise ValueError("user needs name")
        if self.password is None:
            raise ValueError("user needs password")
        if self.username in self.query.filter_by(username=self.username):
            return app.config['REGISTER_ERR']

        db.session.add(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return app.config['ERR_OTHER']
        finally:
            return app.config['REGISTER_RES']

    def check_password(self, password):
        if check_password_hash(self.password, password):
            self.login()
            return app.config['SIGNIN_RES']
        else:
            return app.config['SIGNIN_ERR']
