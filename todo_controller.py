from flask import jsonify, request, make_response
from datetime import datetime
from todo import Todo


todos = []

def get_current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def create_todo():
    req_data = request.get_json()
    print(req_data)
    if not req_data:
        return make_response(jsonify({'error': 'Data not found'}), 400)
    if not all(key in req_data for key in ['title', 'description']):
        return make_response(jsonify({'error': 'Missing required fields'}), 400)
    title = req_data['title']
    description = req_data['description']
    todo_id = len(todos) + 1
    created_date = get_current_time()
    updated_date = None
    deleted_date = None
    finished_date = None
    new_todo = Todo(todo_id, title, description, created_date, updated_date, deleted_date, finished_date)
    todos.append(new_todo)
    return make_response(jsonify({'message': 'Todo created successfully'}), 201)

def get_all_todos():
    if not todos:
        return make_response(jsonify([]), 200)
    return make_response(jsonify([todo.__dict__ for todo in todos]), 200)


def get_todos_by_id(todo_id):
    todo = [todo for todo in todos if todo.id == todo_id and not todo.deleted_date]
    if todo:
        return make_response(jsonify(todo[0].__dict__), 200)
    return make_response(jsonify({'error': 'Todo not found'}), 404)

def delete_todo_by_id(todo_id):
    todo = [todo for todo in todos if todo.id == todo_id and not todo.deleted_date]
    if todo:
        todo[0].deleted_date = get_current_time()
        return make_response(jsonify({'message': 'Todo delete successfully'}), 200)
    return make_response(jsonify({'error': 'Todo not found'}), 404)


def update_todo_by_id(todo_id):
    req_data = request.get_json()
    if not req_data:
        return make_response(jsonify({'error': 'Data not found'}), 400)
    todo = [todo for todo in todos if todo.id == todo_id and not todo.deleted_date]
    if todo:
        todo[0].title = req_data.get('title') or  todo[0].title
        todo[0].description = req_data.get('description') or todo[0].description
        todo[0].updated_date = get_current_time()
        return make_response(jsonify({'message': 'Todo updated successfully'}), 200)
    return make_response(jsonify({'error': 'Todo not found'}), 404)

def finish_todo_by_id(todo_id):
    todo = [todo for todo in todos if todo.id == todo_id and not todo.deleted_date]
    if todo:
        todo[0].finished_date = get_current_time()
        return make_response(jsonify({'message': 'Todo finish successfully'}), 200)
    return make_response(jsonify({'error': 'Todo not found'}), 404)