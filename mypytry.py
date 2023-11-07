import json


def mypy(event, context):
    body = {
        "message": "My Serverless in v3.0! Testing mypy.py!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response