import boto3


def db_insertion(words_dict, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for dictionary in words_dict:
            batch.put_item(
                Item={
                    'word': dictionary['word'],
                    'definition': dictionary['definition'],
                    'word_length': dictionary['word_length']
                }
            )
