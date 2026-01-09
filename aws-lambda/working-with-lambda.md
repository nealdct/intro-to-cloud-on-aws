
# Create a Lambda that logs a message to CloudWatch Logs

1. Create a Lambda function with the Python runtime and the following code

```python
import logging
import json

# Configure the logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Extract the message from the event. Assuming the input is a simple JSON object {"message": "your message here"}
    message = event.get('message', 'No message provided')
    
    # Log the message
    logger.info(message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message logged successfully!')
    }
```

2. Create a test event in the console and add the following test data

```json
{
  "message": "Hello, CloudWatch!"
}
```

3. Run the test and then view the message in CloudWatch Logs
4. Test using the CLI. Create a file in CloudShell named "payload.json" with the following code:

```json
{
  "message": "Hello from CLI!"
}
```
5. Run the following command in AWS CloudShell

```aws lambda invoke --function-name <function-name> --payload fileb://payload.json response.json```

# Create an event notification for S3 upploads

In this exercise we'll modify the function to write the names of files uploaded to an S3 bucket to CloudWatch Logs

1. Update the lambda function code and deploy the update

```python
import json
import logging
import boto3

# Initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the raw event
    logger.info("Event: " + json.dumps(event))
    
    # Process each record within the event
    for record in event['Records']:
        # Extract the bucket name and file key from the event
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        
        # Log the bucket name and file key to CloudWatch
        logger.info(f"New file uploaded: {file_key} in bucket {bucket_name}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Processed S3 upload event successfully!')
    }
```
2. Edit the execution role to add permissions to Lambda to read from S3
3. Create an event notification for all S3 object create events by adding a trigger to AWS Lambda
4. Upload a file and check if a message is written to CloudWatch Logs that includes the file name


