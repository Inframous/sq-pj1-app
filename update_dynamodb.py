import sys
import boto3
from botocore.exceptions import NoCredentialsError

try: 
    assert(len(sys.argv) > 5)
except AssertionError:
    print("Not enough arguments.")
    print("Example usage: ")
    print("python3 update_dynamodb 'table_name' 'ID_Number(int)' 'username' 'date' 'test_result'")
    exit(1)

def update_dynamodb_func(table_name, item_id, username, date, result):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    table.put_item(
        Item={
            'ID': item_id,
            'username': username,
            'date': date,
            'result': result,
        }
    )

args = sys.argv

table_name = args[1]
item_id = int(args[2])
username = args[3]
date = args[4]
result = args[5]

update_dynamodb_func(table_name, item_id, username, date, result)
