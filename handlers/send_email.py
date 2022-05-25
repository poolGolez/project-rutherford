import json

def handler(event, context):

    return {
        "statusCode": 200,
        "headers": {
            "Content-type": "application/json"
        },
        "body": json.dumps(event)
    }
