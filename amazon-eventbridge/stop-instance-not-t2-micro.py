import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    
    # Extract the instance ID from the event
    instance_id = event['detail']['instance-id']
    instance_type = ec2.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['InstanceType']
    
    if instance_type != 't2.micro':
        # Stop the instance
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} stopped because it is not a t2.micro.")
        
    else:
        print(f"Instance {instance_id} is a t2.micro. No action taken.")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function execution completed.')
    }
