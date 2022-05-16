import json
import boto3
import os
import uuid
import datetime

dynamodb = boto3.client("dynamodb")
table_name = os.environ["AWS_USERS_DB_TABLE"]


def handler(event, context):
    request_body = json.loads(event['body'])
    email = request_body['email']
    timestamp = datetime.datetime.now()
    item = {
        "id": str(uuid.uuid4()),
        "email": email,
        "verified": False,
        "timestamp": timestamp.isoformat()
    }

    db_response = dynamodb.put_item(
        TableName=table_name,
        Item=_to_db_item(item)
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "id": str(uuid.uuid4()),
            "email": email,
            "timestamp":  timestamp.isoformat()
        })
    }

def _to_db_item(item):
    db_item = dict()
    for key, value in item.items():
        if  isinstance(value, str):
            db_item[key] = {"S": value}
        elif isinstance(value, bool):
            db_item[key] = {"BOOL": value}

    return db_item