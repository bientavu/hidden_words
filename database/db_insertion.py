import boto3


def db_insertion():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('battle_word')

    response = table.get_item(
        Key={
            'word': 'axeltest',
        }
    )
    item = response['Item']
    print(item)
