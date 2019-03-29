import sys
import pymysql as pm
import pm.err as pex

from app import app, cfg

pm.get_client_info()


def dbSetup():
    connection = pm.connect(host=cfg.DATABASE_HOST,
                            user=cfg.DATABASE_USER,
                            password=cfg.DATABASE_PASS,
                            db=cfg.DATABASE_NAME)
    try:
        pm.db(TODO_DB).table_create('todos').run(connection)
        print('Database setup completed', file=sys.stderr)
    except RqlRuntimeError:
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
