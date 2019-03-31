import sys
import pymysql as pm
import pm.err as pex
from typing import Enum
from datetime import datetime

from app import app, cfg

pm.get_client_info()


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
        _t_id = int(task_id)
        _title = str(title)
        _begin = int(begin)
        _end = int(end)
        _desc = str(description)
        _status = TodoStatus(status)


def dbSetup():
    connection = pm.connect(host=cfg.DATABASE_HOST,
                            user=cfg.DATABASE_USER,
                            password=cfg.DATABASE_PASS,
                            db=cfg.DATABASE_NAME)
    try:
        pm.db(TODO_DB).table_create('todos').run(connection)
        print('Database setup completed', file=sys.stderr)
    except pex:
        print('Database already exists.', file=sys.stderr)
    finally:
        connection.close()

# open connection before each request
@app.before_request
def before_request():
    try:
        pm.connect(host=RDB_HOST, port=RDB_PORT, db=TODO_DB)
    except RqlDriverError:
        abort(503, "Database connection could be established.")
