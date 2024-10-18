from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar tarefas (simulando um "banco de dados")
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')  # Obtém o valor do campo do formulário
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

# Rota para remover uma tarefa
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, port=8080)

