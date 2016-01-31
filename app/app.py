from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<stream_name>', methods=['GET', 'POST'])
def show_stream(stream_name):
    slug = merge_dicts(request.view_args, {'args': request.args})
    return json.dumps(slug)

@app.route('/<stream_name>/<int:drop_id>')
def show_post(stream_name, drop_id):
    slug = merge_dicts(request.view_args, {'args': request.args})
    return json.dumps(slug)

if __name__ == "__main__":
    app.debug = True # rm in prod
    app.run()
