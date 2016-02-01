from flask import Flask
from flask import render_template
from flask import request
import json
import boto3
import datetime
import uuid

application = Flask(__name__)
application.config.from_object('config')

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def save(table, data):
    dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:8000")
    table = dynamodb.Table(table)
    table.put_item(Item=data)

def get_request_data():
    return merge_dicts (
        {'base_url': request.base_url},
        {'uuid': str(uuid.uuid1())},
        request.view_args,
        {'args': request.args}
    )

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/<stream_name>', methods=['GET', 'POST'])
def show_stream(stream_name):
    data = get_request_data()
    save('Drops', data)
    return json.dumps(data)

@application.route('/<stream_name>/<drop_id>')
def show_post(stream_name, drop_id):
    data = get_request_data()
    save('Drops', data)
    return json.dumps(data)

if __name__ == "__main__":
    application.run()
