import os 
from flask import *

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def index():
    data = request.get_json()
    with open('webhook.log', 'a') as f:
        formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
        print(f'Received data: {formatted_data}', file=f)
    return 'Webhook received', 200

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")