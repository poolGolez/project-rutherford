import json

def handler(event, context):
    print("Event", event)

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }