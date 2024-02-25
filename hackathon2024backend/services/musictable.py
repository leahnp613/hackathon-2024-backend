import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Music',
    KeySchema=[
        {
            'AttributeName': 'PK',
            'KeyType': 'HASH'  # Partition key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'PK',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='Music')