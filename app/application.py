from flask import Flask
from flask import render_template
from flask import request
import json
import boto3
import datetime

application = Flask(__name__)
application.config.from_object('config')

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def put_data(table, blob):
    dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:8000")
    table = dynamodb.Table(table)
    table.put_item(
        Item={
           'drop_id': str(datetime.datetime.now())
        }
    )

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/<stream_name>', methods=['GET', 'POST'])
def show_stream(stream_name):
    slug = merge_dicts(request.view_args, {'args': request.args})
    put_data('Drops', slug)
    return json.dumps(slug)

@application.route('/<stream_name>/<drop_id>')
def show_post(stream_name, drop_id):
    slug = merge_dicts(request.view_args, {'args': request.args})
    put_data(slug)
    return json.dumps('Drops', slug)

if __name__ == "__main__":
    application.run()
