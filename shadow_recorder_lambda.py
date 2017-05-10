#this lambda function is fired by a shadow update rule for the thing "jio2"
# it stores the client token and activatated state (active, inactive) in DynamoDB
# Eventually, it will store the activation time series info (thing, state, timestamp, lat/long).
# so as to enable a BI interface to test where and how the tag is being used

import logging
import boto3
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    # TODO implement
    #logger.info('got event {}'.format(event))
    logger.info('got event state {}, token {}'.format(event['state']['desired']['active'],event['clientToken']))
    #logger.info('got context{}'.format(context))
    
    ddb = boto3.client('dynamodb')
    response = ddb.put_item(TableName='sampleTable',Item={'topic':{'S':event['clientToken']},'timestamp':{'S':'1245P'}})
    print(response)
    
    return 'Hello from jb shadow update recorder Lambda'
