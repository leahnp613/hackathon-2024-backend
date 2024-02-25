import json
import boto3
from models import Music

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Music')

def lambda_handler(event, context):
    # Parse the JSON body of the event
    body = json.loads(event['body'])

    # Validate and parse the data as a Music object
    music = Music(**body)

    # Check the HTTP method to determine whether to save or delete music
    http_method = event['httpMethod']

    if http_method == 'POST':
        # Save the music data to the database
        table.put_item(Item=music.dict())
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Music saved successfully',
            }),
        }
    elif http_method == 'DELETE':
        # Delete the music data from the database
        table.delete_item(Key={'id': music.id})
        response = {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Music deleted successfully',
            }),
        }
    else:
        # Unsupported HTTP method
        response = {
            'statusCode': 400,
            'body': json.dumps({
                'message': f'Unsupported HTTP method: {http_method}',
            }),
        }

    response['headers'] = {'Content-Type': 'application/json'}
    return response