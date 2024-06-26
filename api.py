from flask import Flask, request

app = Flask(__name__)

@app.route('/function1', methods=['GET', 'POST'])
def function1():
    if request.method == 'GET':
        # This is a GET request
        return 'This is a test'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

    