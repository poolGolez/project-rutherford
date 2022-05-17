import json
import boto3
import os
import uuid
import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.client("dynamodb")
table_name = os.environ["AWS_USERS_DB_TABLE"]


def handler(event, context):
    request_body = json.loads(event['body'])
    email = request_body['email']

    try:
        item = save_db_record(email)
        return ok_response(item)
    except ClientError as error:
        return error_response(error)


def save_db_record(email):
    timestamp = datetime.datetime.now()
    item = {
        "PK": str(uuid.uuid4()),
        "email": email,
        "verified": False,
        "timestamp": timestamp.isoformat()
    }

    dynamodb.transact_write_items(
        TransactItems=[
            {
                "Put": {
                    "TableName": table_name,
                    "Item": to_db_item(item)
                }
            },
            {
                "Put": {
                    "TableName": table_name,
                    "Item": to_db_item({"PK": f"EMAIL#{email}"}),
                    "ConditionExpression": "attribute_not_exists(#pk)",
                    "ExpressionAttributeNames": {"#pk": "PK"},
                }
            }
        ]
    )

    return item


def to_db_item(item):
    db_item = dict()
    for key, value in item.items():
        if isinstance(value, str):
            db_item[key] = {"S": value}
        elif isinstance(value, bool):
            db_item[key] = {"BOOL": value}

    return db_item


def ok_response(item):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(item)
    }


def error_response(error):
    print(error)
    return {
        "statusCode": 422,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": str(error)})
    }
