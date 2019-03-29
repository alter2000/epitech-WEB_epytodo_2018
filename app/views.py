from flask import render_template, request, jsonify
import json

from app import app


# index route, shows index.html view
@app.route('/')
def index():
    return render_template('index.html')


# endpoint for storing todo item
@app.route('/add-todo', methods=['POST'])
def addTodo():
    data = json.loads(request.data)  # load JSON data from request
    return jsonify(data)


# endpoint for deleting todo item
@app.route('/remove-todo/<item_id>')
def removeTodo(item_id):
    return jsonify({
                    'id': item_id,
                   })


# endpoint for updating todo item
@app.route('/update-todo/<item_id>', methods=['POST'])
def updateTodo(item_id):
    data = {
            'id': item_id,
            'completed': json.loads(request.data).get('completed', 0)
            }
    return jsonify(data)
