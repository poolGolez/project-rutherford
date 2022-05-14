import json
import boto3

s3 = boto3.resource('s3')
bucket_name = 'project-rutherford-65819'
object_key = 'quotes.json'

def handler(event, context):
    print("Event", event)
    s3_object = s3.Object(bucket_name, object_key).get()
    file_contents = s3_object['Body'].read().decode("utf-8")
    quotes_json = json.loads(file_contents)

    return {
        "statusCode": 200,
        "body": json.dumps(quotes_json)
    }
