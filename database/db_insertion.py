import boto3
from constants import TABLE_NAME


def db_insertion(words_dict):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    with table.batch_writer() as batch:
        for dictionary in words_dict:
            batch.put_item(
                Item={
                    'word': dictionary['word'],
                    'definition': dictionary['definition'],
                    'word_length': dictionary['word_length']
                }
            )

    # response = table.get_item(
    #     Key={
    #         'word': 'axeltest',
    #     }
    # )
    #
    # item = response['Item']
    # print(item)
