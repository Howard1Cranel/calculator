import os
import json
import subprocess
from flask import request

def execute(command):
    process = subprocess.Popen(command, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8') # Декодируем байты в строки

def setup_webhook_route(app):
    """Настраивает маршрут вебхука."""

    @app.route('/webhook', methods=['POST'])
    def webhook():
        data = request.get_json()

        # Логирование полученных данных в файл
        try:
            with open('webhook.log', 'a') as f:
                formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
                print(f'Received {formatted_data}', file=f)
        except IOError as e:
            print(f'Error writing to webhook.log: {e}')

        try:
            repo_url = data["repository"]["clone_url"]  # используем clone_url
            # Директория, в которой расположен ваш сайт
            repo_dir = '/home/calculator'

            # Переходим в директорию репозитория и выполняем команду git pull
            # Используем execute для получения stdout и stderr
            stdout, stderr = execute(f"cd {repo_dir} && git pull origin main")  # Замените main, если используете другую ветку
            print(f'Successfully updated repository in {repo_dir}')
            print(f'Git pull output: {stdout}')
            if stderr:
                print(f'Git pull error: {stderr}')

            return 'Webhook received and update triggered', 200

        except KeyError as e:
            print(f'Error processing webhook Missing key {e}')
            return f'Error processing webhook Missing key {e}', 400  # Bad Request
        except Exception as e:
            print(f'Error updating repository: {e}')
            return f'Error updating repository: {e}', 500  # Internal Server Error