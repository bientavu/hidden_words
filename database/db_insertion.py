import boto3


def db_insertion(words_dict):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('battle_word')

    for dictionary in words_dict:
        table.put_item(
            Item={
                'word': dictionary['word'],
                'definition': dictionary['definition']
            }
        )

    response = table.get_item(
        Key={
            'word': 'axeltest',
        }
    )

    item = response['Item']
    print(item)
