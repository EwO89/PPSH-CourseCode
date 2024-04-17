
## Задача 1


import random
from flask import Flask

app = Flask(__name__)


@app.route('/random-quote')
def random_quote():
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
    return random_quote


if __name__ == '__main__':
    app.run()


## Задача 2


from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/convert-temperature', methods=['POST'])
def convert_temperature():
    celsius = request.json.get('celsius')

    if celsius is None:
        return jsonify({'error': 'Missing celsius value'}), 400

    fahrenheit = celsius * 9 / 5 + 32

    return jsonify({'fahrenheit': fahrenheit}), 200


if __name__ == '__main__':
    app.run(debug=True)

## Задача 3


from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    if not title or not description:
        return jsonify({'message': 'Недостаточно данных'}), 400

    new_task = {
        'task_id': len(tasks) + 1,
        'title': title,
        'description': description
    }
    tasks.append(new_task)

    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['task_id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Задача не найдена'}), 404

    tasks.remove(task)

    return jsonify({'message': 'Задача успешно удалена'}), 200


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200


if __name__ == '__main__':
    app.run()


