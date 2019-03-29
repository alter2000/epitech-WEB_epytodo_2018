from flask import jsonify


class Config(object):
    DATABASE_NAME = "epytodo"
    DATABASE_HOST = "localhost"
    DATABASE_SOCK = "/run/mysqld/mysqld.sock"
    DATABASE_USER = "mysql"
    DATABASE_PASS = "asdf"


class Globals(object):
    ERR_NOLOGIN = jsonify({'error': 'you must be logged in'})
    ERR_NOTID = jsonify({'error': 'task id does not exist'})
    ERR_OTHER = jsonify({'error': 'internal error'})

    REGISTER_RES = jsonify({'result': 'account created'})
    REGISTER_ERR = jsonify({'error': 'account already exists'})

    SIGNIN_RES = jsonify({'result': 'signin successful'})
    SIGNIN_ERR = jsonify({'error': 'login or password does not match'})

    SIGNOUT_RES = jsonify({'result': 'signout successful'})
    SIGNOUT_ERR = jsonify({'error': 'internal error'})

    TASK_ID_MOD_RES = jsonify({'result': 'update done'})

    TASK_ID_ADD_RES = jsonify({'result': 'new task added'})

    TASK_ID_DEL_RES = jsonify({'result': 'task deleted'})
