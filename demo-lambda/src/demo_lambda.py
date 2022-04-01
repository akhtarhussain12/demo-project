import json

def main(event, context):
    try:
        new_message = {
            "event_id" : "abc",
            "event_name" : "newEvent",
            "event_date" : "date"
        }
        message = json.dumps(new_message)

    except Exception:
        message = "Oops! something went wrong."

    return message


import boto3
from uuid import uuid4
def main(event, context):
    sqs = boto3.client("sqs")
    dynamodb = boto3.resource('dynamodb')
    for record in event['Records']:
        event_id = record['eventID']
        event_name = record['eventName']
        event_date = record['eventDate']
        demo_table = dynamodb.Table('demoTable')
        demo_table.put_item(Item={'Unique': str(uuid4()), 'ID': event_id, 'Event': event_name, 'Date': event_date})

    return demo_table
