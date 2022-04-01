import json
# import boto3

def main(event, context):
    # sqs = boto3.client("sqs")
    # dynamodb = boto3.resource('dynamodb')
    message = {
        "event_id" : "abc",
        "event_name" : "newEvent",
        "event_date" : "date"
    }

    print(json.dumps(message))

    response = {
        "status_code" : 200,
        "message" : json.dumps(message)
    }

    return response


# import boto3
# from uuid import uuid4
# def main(event, context):
#     try:
#         sqs = boto3.client("sqs")
#         dynamodb = boto3.resource('dynamodb')
#         for record in event['Records']:
#             message_name = record['sqs']['message']['name']
#             object_key = record['sqs']['object']['key']
#             size = record['sqs']['object'].get('size', -1)
#             event_id = record['eventID']
#             event_name = record['eventName']
#             event_date = record['eventDate']
#             dynamo_table = dynamodb.Table('demoTable')
#             dynamo_table.put_item(Item={'Unique': str(uuid4()), 'Name': message_name, 'Object': object_key, 'Size': size, 'ID': event_id, 'Event': event_name, 'Date': event_date})
#
#     except:
#         pass