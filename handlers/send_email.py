import json
import boto3
import random


def load_quotes():
    s3 = boto3.resource("s3")
    bucket_name = "project-rutherford-65819"
    object_key = "quotes.json"
    s3_object = s3.Object(bucket_name, object_key).get()
    file_contents = s3_object['Body'].read().decode("utf-8")
    print("Loading quotes")
    return json.loads(file_contents)["quotes"]


quotes = load_quotes()
def handler(event, context):
    quote = pick_quote()

    return {
        "statusCode": 200,
        "headers": {
            "Content-type": "application/json"
        },
        "body": json.dumps({
            "quote": quote
        })
    }


def pick_quote():
    index = random.randint(0, len(quotes) - 1)
    quote = quotes[index]

    return quote
