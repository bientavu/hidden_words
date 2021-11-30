import boto3
from moto import mock_dynamodb2
from decimal import Decimal
from database.db_insertion import db_insertion


@mock_dynamodb2
def test_db_insertion():
    dynamodb = boto3.resource('dynamodb')
    table_name = 'test'
    table = dynamodb.create_table(TableName=table_name,
                                  KeySchema=[{'AttributeName': 'word_length',
                                              'KeyType': 'HASH'}],
                                  AttributeDefinitions=[
                                      {'AttributeName': 'word_length',
                                       'AttributeType': 'N'}])
    data = [
        {'word_length': Decimal('6'), 'word': 'HELLOO', 'definition': 'AA'},
        {'word_length': Decimal('5'), 'word': 'WORLD', 'definition': 'BB'},
        {'word_length': Decimal('3'), 'word': 'LOL', 'definition': 'CC'}
    ]
    db_insertion(data, table_name)
    response = table.get_item(Key={'word_length': data[2]['word_length']})
    actual_output = response['Item']

    assert actual_output is not None
    assert actual_output == data[2]
    assert actual_output['word'] == data[2]['word']
