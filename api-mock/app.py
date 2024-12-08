from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados
tasks = [
    {"id": 1, "text": "Estudar Flask", "completed": False},
    {"id": 2, "text": "Fazer compras", "completed": False},
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
