from flask import jsonify, request, make_response
from datetime import datetime
from todo import Todo
from schemaValidate import CreateTodoInputs, UpdateTodoInputs


todos = []

def get_current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def create_todo():
    req_data = request.get_json()
    inputs = CreateTodoInputs(request)
    if inputs.validate():
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
    else: 
        return make_response(jsonify({'error': inputs.errors}), 400)

def get_all_todos():
    if not todos:
        return make_response(jsonify([]), 200)
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    
    start_index = (page - 1) * limit
    end_index = start_index + limit
    print(start_index)
    print(end_index)
    return make_response(jsonify([todo.__dict__ for todo in todos[start_index:end_index]]), 200)


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
    inputs = UpdateTodoInputs(request)
    if inputs.validate():
        todo = [todo for todo in todos if todo.id == todo_id and not todo.deleted_date]
        if todo:
            todo[0].title = req_data.get('title') or  todo[0].title
            todo[0].description = req_data.get('description') or todo[0].description
            todo[0].updated_date = get_current_time()
            return make_response(jsonify({'message': 'Todo updated successfully'}), 200)
        else:
            return make_response(jsonify({'error': 'Todo not found'}), 404)
    else:
        return make_response(jsonify({'error': inputs.errors}), 400)

def finish_todo_by_id(todo_id):
    todo = [todo for todo in todos if todo.id == todo_id and not todo.deleted_date]
    if todo:
        todo[0].finished_date = get_current_time()
        return make_response(jsonify({'message': 'Todo finish successfully'}), 200)
    return make_response(jsonify({'error': 'Todo not found'}), 404)