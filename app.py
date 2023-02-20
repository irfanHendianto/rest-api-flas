from flask import Flask, jsonify
from config import Config
from routes import todo_routes

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(todo_routes)


@app.route('/')
def hello():
   response = {
        "message": "Hello, world!"
   }
   return jsonify(response)


if __name__ == '__main__':
    app.run(port=app.config['PORT'],debug=app.config['DEBUG'])