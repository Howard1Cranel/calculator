import os
import json
import subprocess
from flask import Flask, render_template, request
from flask_restx import Api, Resource


app = Flask(__name__)
api = Api(app)

def welcome():
    return render_template('form.html')

def add(var_1, var_2):
    return var_1 + var_2

def subtract(var_1, var_2):
    return var_1 - var_2

def multiply(var_1, var_2):
    return var_1 * var_2

def divide(var_1, var_2):
    if var_2 == 0:
        return 0
    else:
        return var_1 / var_2

def minimum(var_1, var_2):
    return min(var_1, var_2)

def maximum(var_1, var_2):
    return max(var_1, var_2)

def degree(var_1, var_2):
    return var_1 ** var_2

@app.route('/', methods=['GET', 'POST'])
@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            # Отладочный вывод значений
            print(f'num1: {num1}, num2: {num2}, operation: {operation}')
            
            operations = {
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
                '**': degree,
                'max': maximum,
                'min': minimum
            }
            
            if operation in operations:
                result = operations[operation](num1, num2)
            else:
                result = 'Ошибка: Неизвестная операция'
        except ValueError:
            result = 'Ошибка: Введите корректные числа'
    
    # Отладочный вывод результата
    print(f'Результат: {result}')
    
    return render_template('form.html', result=result)
    
@app.route('/webhook', methods=['POST'])    
def webhook():
    data = request.get_json()

    # Логирование полученных данных в файл
    with open('webhook.log', 'a') as f:
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        print(f'Received data: {formatted_data}', file=f)

    # Директория, в которой расположен ваш сайт
    repo_dir = '/home/calculator'
    
    # Переходим в директорию репозитория и выполняем команду git pull
    try:
        subprocess.run(['git', 'pull'], cwd=repo_dir, check=True)
        print(f'Successfully updated repository in {repo_dir}')
    except subprocess.CalledProcessError as e:
        print(f'Error updating repository: {e}')

    return 'Webhook received and update triggered', 200
    

if __name__ == '__main__':
    app.run(debug=True, port=5000,host='0.0.0.0')
