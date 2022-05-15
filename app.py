from flask import Flask, abort, render_template, request, redirect, url_for
import uuid

from file import writeJson, readJson


app = Flask(__name__)

@app.route('/')
def index():
    todos = readJson("data/todos.json", {})

    return render_template('index.html.j2', todos=enumerate(todos.items()))

@app.route('/add', methods=['GET', 'POST'])
def addTodo():
    errors = []

    if request.method == "POST":
        description = request.form.get('description', '')

        if description != '':
            id = str(uuid.uuid4())

            todos = readJson("data/todos.json", {})

            todos[id] = {
                'description': description,
                'status': 'opened'
            }

            writeJson("data/todos.json", todos)

            return redirect(url_for('index'))
        else:
            errors.append('Informe a descrição.')

    return render_template('add.html.j2', errors=errors)

@app.route('/edit/<uuid:id>', methods=['GET', 'POST'])
def editTodo(id):
    id = str(id)

    todos = readJson("data/todos.json", {})

    if id not in todos:
        abort(404)

    todo = todos[id]

    errors = []

    if request.method == "POST":
        description = request.form.get('description', '')
        status = request.form.get('status', todo['status'])

        if status not in ['opened', 'closed']:
            errors.append("Informe um status válido.")
        elif not description:
            errors.append("Informe a descrição.")
            todo['description'] = ''
            todo['status'] = status
        else:
            todos = readJson("data/todos.json", {})

            todos[id] = {
                'description': description,
                'status': status
            }

            writeJson("data/todos.json", todos)

            return redirect(url_for('index'))

    return render_template('edit.html.j2', todo=todo, errors=errors)

@app.route("/<id>", methods=["DELETE"])
def removeTodo(id):
    todos = readJson("data/todos.json", {})

    if id not in todos:
        abort(404)

    del todos[id]

    writeJson("data/todos.json", todos)

    return "success"

@app.route("/<id>/toggleStatus", methods=["POST"])
def toggleStatus(id):
    todos = readJson("data/todos.json", {})

    if id not in todos:
        abort(404)

    todo = todos[id]
    todo['status'] = 'closed' if todo['status'] == 'opened' else 'opened'

    writeJson("data/todos.json", todos)

    return "success"

if __name__ == "__main__":
    app.run()