import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
    signature_version = 'v4',
    retries = {
        'max_attempts' : 10,
        'mode' : 'standard'
    }
)

client = boto3.client('dynamodb')

dynamodb = boto3.resource('dynamodb')

table = client.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# table.put_item(
#     Item={
#         'username':'el_plz',
#         'first_name':'christian',
#         'last_name':'oviedo'
#     }
# )

table.wait_until_exists()

print(table.item_count)
