from flask import Flask, render_template, request

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
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

@app.route('/', methods=['POST'])
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
    app.run(debug=True)
