from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<stream_name>', methods=['GET', 'POST'])
def show_stream(stream_name):
    if request.method == 'POST':
        pass
    else:
        return json.dumps({'stream_name': stream_name})
    return render_template('stream.html', stream_name=stream_name)

@app.route('/<stream_name>/<int:drop_id>')
def show_post(stream_name, drop_id):
    return json.dumps({'stream_name': stream_name, 'drop_id': drop_id})

if __name__ == "__main__":
    app.debug = True # rm in prod
    app.run()
