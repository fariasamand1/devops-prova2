from flask import Flask, jsonify

app = Flask(__name__)

# Lista de tarefas
tasks = [
    {"id": 1, "text": "Comprar leite", "completed": False},
    {"id": 2, "text": "Estudar para a prova", "completed": True},
    {"id": 3, "text": "Lavar a roupa", "completed": False},
]

# Rota para retornar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Rota para retornar uma tarefa específica pelo ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((t for t in tasks if t['id'] == id), None)
    return jsonify(task) if task else ('', 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Certificando que o app aceita conexões externas
