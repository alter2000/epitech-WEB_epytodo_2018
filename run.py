from app import app
from app.models import User, Task


@app.shell_context_processor
def mkcontext():
    return {'db': app.db, 'User': User, 'Task': Task}


if __name__ == "__main__":
    app.run(debug=True)
