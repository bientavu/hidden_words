import boto3
import pytest
import requests
from decimal import Decimal
from database.dictionary_parser import DictionaryCleaner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from moto import mock_dynamodb2
from database.db_insertion import db_insertion


@pytest.fixture()
def response():
    return requests.get("https://dictionnaire.lerobert.com/explore/def/X")


@pytest.fixture()
def dict_cleaner():
    dict_cleaner = DictionaryCleaner()
    return dict_cleaner


@pytest.fixture()
def server():
    """Selenium web driver setup"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    selenium = webdriver.Chrome(service=service, options=chrome_options)
    selenium.implicitly_wait(10)
    return selenium


@pytest.fixture()
def fake_dynamo_db():
    with mock_dynamodb2():
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
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
            {'key': Decimal('1'), 'word': 'LOL', 'definition': 'CC'},
            {'key': Decimal('1'), 'word': 'HAHAHA', 'definition': 'DD'},
            {'key': Decimal('1'), 'word': 'BONJOUR', 'definition': 'EE'}
        ]

        db_insertion(data, table_name)
        response = table.get_item(Key={'key': data[2]['key']})

        response_for_query = table.query(
            TableName=table_name,
            KeyConditionExpression="#DDB_key = :pkey",
            ExpressionAttributeValues={
                ":pkey": 1
            },
            ExpressionAttributeNames={
                "#DDB_key": "key"
            },
        )

        return dynamodb, table_name, table, data, response, response_for_query
