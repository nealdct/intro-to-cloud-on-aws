# Serverless Application with REST API – Part 1

## 1. Create the first Lambda function

1. Create a Lambda function with the following settings
- Name: SubmitOrderFunction
- Python 3.9 runtime

2. Add the code from the `SubmitOrderFunction.py` file
3. Add the `AmazonSQSFullAccess` permissions policy to the execution role

***you need to come back and add the queue URL shortly***

## 2. Create the SQS queue

1. Create an SQS queue
2. Use the standard queue type
3. Name it: `ProductOrdersQueue`
4. Copy the queue URL and add it to line 5 of the SubmitOrderFunction code
5. Deploy the Lambda function

## 3. Test order submissions

1. In Lambda create and submit a test event with the following data

```json
{
  "body": "{\"productName\":\"Test Product\",\"quantity\":3}"
}
```

2. Go to SQS and poll for messages - you should see a message waiting the queue

## 4. Create the processing function

1. Create a Lambda function with the following settings
- Name: ProcessOrderFunction
- Python 3.9 runtime

2. Add the code from the `ProcessOrderFunction.py` file
3. Add the `AmazonSQSFullAccess` and `AmazonDynamoDBFullAccess` permissions policies to the execution role

## 5. Create the DynamoDB table

1. Create a DynamoDB table with the following settings
- Name: ProductOrders
- Primary key: orderId

## 6. Deploy and test the application

1. Add the table name to line 6 of the ProcessOrderFunction function code
2. Go to SQS and configure a Lambd trigger and specify the ProcessOrderFunction
3. Check the DynamoDB table to see if the first test event was processed
4. Test using the CLI. Using CloudShell create a file named `input.json` with the following contents

```json
{
  "body": "{\"productName\":\"Test Product 2\",\"quantity\":2}"
}
```

5. Invoke the function:

```bash
aws lambda invoke --function-name <function-name> --payload fileb://input.json output.json
```

# Serverless Application with REST API – Part 2

## 1. Create the API

1. Create a REST API in the API Gateway Console named `ProductOrdersAPI`
2. Create a new resource `/orders` and enable CORS
3. Create a `POST` method for `/orders` integrated with the `SubmitOrderFunction`
4. Enable a Lambda proxy integration
5. Click back up to the `/orders` resource and click "Enable CORS"
6. Select all CORS options
7. Deploy your API to a new stage named `prod`
8. Update the invoke URL in the index.html file on line 32 where it says `YOUR_API_ENDPOINT`

***note, the invoke URL on line 32 should include /prod/orders on the end and look like this example***

'https://v1grynidwb.execute-api.us-east-1.amazonaws.com/prod/orders'

## 2. Create the static website bucket and test the application

1. In Amazon S3 create a bucket
2. Configure the bucket for static website hosting
3. Set the default document to `index.html`
4. Enable public access using a bucket policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "<YOUR-BUCKET-ARN>/*"
        }
    ]
}
```

5. Upload the edited index.html that has the API endpoint URL configured
6. Navigate to the static website endpoint
7. Submit some order information and check it is added to the DynamoDB table
8. If you do not receive an "Order submitted successfully!" response, use your browsers Developer Tools to troubleshoot





