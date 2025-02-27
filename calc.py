import os
import json
import subprocess
from flask import Flask, render_template, request
# from flask_restx import Api, Resource #Удаляем, так как не используем

# Импортируем функции из webhook.py
from webhook import setup_webhook_route

app = Flask(__name__)
# api = Api(app) #Удаляем, так как не используем

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    if number_2 == 0:
        return 'Ошибка: Деление на ноль'
    return number_1 / number_2

def degree(number_1, number_2):
    return number_1 ** number_2

def maximum(number_1, number_2):
    return max(number_1, number_2)

def minimum(number_1, number_2):
    return min(number_1, number_2)
    
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



if __name__ == '__main__':
    # Настраиваем маршрут вебхука, передавая app
    setup_webhook_route(app)
    app.run(debug=True, port=5000, host='0.0.0.0')