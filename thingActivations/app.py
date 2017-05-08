# map backend written in Chalice
# to be used by a D3.js frontend that can look at all or device-specific
# activations of tags

from chalice import Chalice
from chalice import BadRequestError
from decimal import Decimal
import boto3
from boto3.dynamodb.conditions import Key, Attr

app = Chalice(app_name='thingActivations')
app.debug = True

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Activations')

def pois_from_db(thing_id):
    db_results = table.query(
        KeyConditionExpression=Key('thingId').eq(thing_id)
        )
    if db_results['Count'] == 0:
        return False
    else:
        return db_results['Items']

@app.route('/thing/{thing_id}')
def index(thing_id):
    activations = pois_from_db(thing_id)
    return {'activations': activations}


@app.route('/')
def index():
    return {'hello': 'world'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return {'user_id': user_id}
#
# See the README documentation for more examples.
#
