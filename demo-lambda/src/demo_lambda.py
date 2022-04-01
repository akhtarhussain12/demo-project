import json
import boto3
import os
from uuid import uuid4

evars = os.environ


def process_data(event_id):
    # dynamodb = boto3.resource('dynamodb')
    return 'success'


def main(event, context):
    """
    Args:
		event: Event payload
		context: system context
    """
    try:
        event_id = event['event_id']
        response = process_data(event_id)

    except Exception as e:
        print(f"Error calling Lambda : {str(e)}")
        response = 'failure'

    return response