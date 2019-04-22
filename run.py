from app import app, db
from app.models import User, Task


@app.shell_context_processor
def mkcontext():
    return {'db': db, 'User': User, 'Task': Task}


if __name__ == "__main__":
    # run Flask app in debug mode
    app.run(debug=True)
