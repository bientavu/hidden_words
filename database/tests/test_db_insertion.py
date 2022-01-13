from moto import mock_dynamodb2


@mock_dynamodb2
def test_db_insertion(fake_dynamo_db):
    """
    Test to check if the db_insertion is correct,
    for this we use the dynamodb2 mock library.
    """
    actual_output = fake_dynamo_db[4]['Item']

    assert actual_output is not None
    assert actual_output == fake_dynamo_db[3][4]
    assert actual_output['word'] == fake_dynamo_db[3][4]['word']
