
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# List to store tasks (in memory)
tasks = []

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        tasks.append({'name': task_name, 'done': False})
    return redirect(url_for('index'))

# Route to mark a task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['done'] = True
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)



# Explanation:

# Flask setup: We initialize a Flask app with app = Flask(__name__).
# Task list: For simplicity, we’re storing tasks in a Python list (tasks). Each task is a dictionary with a name and done status.
# Routes:
# /: Displays all tasks.
# /add: Handles adding a new task via a POST request.
# /complete/<task_id>: Marks a task as completed.
# /delete/<task_id>: Deletes a task.