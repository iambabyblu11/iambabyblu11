app.py
pip install flask
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True)
from flask import send_from_directory

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
