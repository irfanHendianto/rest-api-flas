from flask import Blueprint
from todo_controller import get_all_todos, create_todo, get_todos_by_id, delete_todo_by_id, update_todo_by_id, finish_todo_by_id

todo_routes = Blueprint('todo_routes', __name__)

# create todo
todo_routes.route('/api/todos/', methods=['POST'])(create_todo)

# get all todos
todo_routes.route('/api/todos/', methods=['GET'])(get_all_todos)

# get todos by id
todo_routes.route('/api/todos/<int:todo_id>', methods=['GET'])(get_todos_by_id)

# delete todo by id
todo_routes.route('/api/todos/<int:todo_id>', methods=['DELETE'])(delete_todo_by_id)

# update todo by id
todo_routes.route('/api/todos/<int:todo_id>', methods=['PUT'])(update_todo_by_id)

# finish todo by id
todo_routes.route('/api/todos-finish/<int:todo_id>', methods=['PUT'])(finish_todo_by_id)

