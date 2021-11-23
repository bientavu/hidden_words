import boto3
from constants import TABLE_NAME
from boto3.dynamodb.conditions import Key, Attr


def load_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print(data)
    return data


def get_words_by_length(all_words, length):
    words_by_length = []


