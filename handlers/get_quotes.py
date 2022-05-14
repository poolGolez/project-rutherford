import json
import boto3

s3 = boto3.resource('s3')

def handler(event, context):
    print("Event", event)
    s3_object = s3.Object('project-rutherford-65819', 'quotes.json').get()
    file_contents = s3_object['Body'].read().decode("utf-8")
    print("S3 Object:", file_contents)

    return {
        "statusCode": 200,
        "body": json.dumps(json.loads(file_contents))
    }
