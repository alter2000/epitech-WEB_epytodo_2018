class Config(object):
    DATABASE_NAME = "epytodo"
    DATABASE_HOST = "localhost"
    DATABASE_SOCK = "/run/mysqld/mysqld.sock"
    DATABASE_USER = "mysql"
    DATABASE_PASS = "asdf"


class Globals(object):
    ERR_NOLOGIN = {'error': 'you must be logged in'}
    ERR_NOTID = {'error': 'task id does not exist'}
    ERR_OTHER = {'error': 'internal error'}

    REGISTER_RES = {'result': 'account created'}
    REGISTER_ERR = {'error': 'account already exists'}

    SIGNIN_RES = {'result': 'signin successful'}
    SIGNIN_ERR = {'error': 'login or password does not match'}

    SIGNOUT_RES = {'result': 'signout successful'}
    SIGNOUT_ERR = {'error': 'internal error'}

    TASK_ID_MOD_RES = {'result': 'update done'}

    TASK_ID_ADD_RES = {'result': 'new task added'}

    TASK_ID_DEL_RES = {'result': 'task deleted'}
