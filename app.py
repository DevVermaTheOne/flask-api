from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__,template_folder="templates")

api = Api(app)

todos = {
    1: {"task":"Letter", "summary":"write a letter to your friend"},
    2: {"task":"task 2", "summary":"summary of task 2"},
    3: {"task":"task 3", "summary":"summary of task 3"},
    4: {"task":"task 4", "summary":"summary of task 4"},
}

class Todo(Resource):
    def get(self, todo_id):
        return todos[todo_id]

class Todos(Resource):
    def get(self):
        return todos
    
api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(Todos, "/todos")


if __name__=='__main__':
    app.run(debug=True)
