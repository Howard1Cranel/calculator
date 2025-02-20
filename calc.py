from flask import Flask, render_template, request
from flask import request, render_template


app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 / num2

def minimum(num1, num2):
    return min(num1, num2)

def maximum(num1, num2):
    return max(num1, num2)

def degree(num1, num2):
    return num1 ** num2

def result():
    var_1 = request.form.get("var_1", type=int, default=0)
    var_2 = request.form.get("var_2", type=int, default=0)
    operation = request.form.get("operation")

    if operation == 'Addition':
        result = add(var_1, var_2)
    elif operation == 'Subtraction':
        result = subtract(var_1, var_2)
    elif operation == 'Multiplication':
        result = multiply(var_1, var_2)
    elif operation == 'Division':
        result = divide(var_1, var_2)
    elif operation == 'Minimum':
        result = minimum(var_1, var_2)
    elif operation == 'Maximum':
        result = maximum(var_1, var_2)
    elif operation == 'Degree':
        result = degree(var_1, var_2)
    else:
        result = 0

    entry = result
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
    