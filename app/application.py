from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json
import boto3
import datetime
import uuid
import decimal
from boto3.dynamodb.conditions import Key, Attr

application = Flask(__name__)
application.config.from_object('config')

@application.route('/')
def index():
    return jsonify({'site_message': 'Welcome to flood.'})

@application.route('/<stream_name>', methods=['GET', 'POST'])
def show_stream(stream_name):
    data = get_request_data()
    save('Drops', data)
    response = get_posts('Drops', data['base_url'])
    return jsonify(**response)

@application.route('/<stream_name>/<drop_id>')
def show_post(stream_name, drop_id):
    data = get_request_data()
    return jsonify(data)

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def get_posts(table, base_url):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
    table = dynamodb.Table(table)
    return table.query(
        KeyConditionExpression=Key('base_url').eq(base_url)
    )

def save(table, data):
    dynamodb = boto3.resource('dynamodb',endpoint_url="http://localhost:8000")
    table = dynamodb.Table(table)
    table.put_item(Item=data)

def get_request_data():
    return merge_dicts (
        {'base_url': request.base_url},
        {'drop_id': str(uuid.uuid1())},
        request.view_args,
        {'args': request.args}
    )

if __name__ == "__main__":
    application.run()
