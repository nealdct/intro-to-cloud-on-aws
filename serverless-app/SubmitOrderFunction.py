import json
import boto3

sqs = boto3.client('sqs')
queue_url = 'YOUR_SQS_QUEUE_URL'

def lambda_handler(event, context):
    try:
        order_details = json.loads(event['body'])
        response = sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(order_details))
        return {'statusCode': 200, 'headers': {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Allow-Methods': 'OPTIONS,POST'}, 'body': json.dumps({'message': 'Order submitted to queue successfully'})}
    except Exception as e:
        return {'statusCode': 400, 'body': json.dumps({'error': str(e)})}
