from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    f = open('data.txt', 'w')
    print(json_data, file=f)
    f.flush()
    f.close()
    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')