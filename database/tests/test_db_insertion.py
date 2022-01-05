import boto3
from moto import mock_dynamodb2
from decimal import Decimal
from database.db_insertion import db_insertion


@mock_dynamodb2
def test_db_insertion():
    dynamodb = boto3.resource('dynamodb')
    table_name = 'test'
    table = dynamodb.create_table(TableName=table_name,
                                  KeySchema=[{'AttributeName': 'key',
                                              'KeyType': 'HASH'}],
                                  AttributeDefinitions=[
                                      {'AttributeName': 'key',
                                       'AttributeType': 'N'}])
    data = [
        {'key': Decimal('1'), 'word': 'HELLOO', 'definition': 'AA'},
        {'key': Decimal('1'), 'word': 'WORLD', 'definition': 'BB'},
        {'key': Decimal('1'), 'word': 'LOL', 'definition': 'CC'}
    ]
    db_insertion(data, table_name)
    response = table.get_item(Key={'key': data[2]['key']})
    actual_output = response['Item']

    assert actual_output is not None
    assert actual_output == data[2]
    assert actual_output['word'] == data[2]['word']
