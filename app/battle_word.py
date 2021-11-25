from pprint import pprint
import random
import board
import boto3
import numpy
from constants import TABLE_NAME
from boto3.dynamodb.conditions import Key, Attr


def get_words_by_length(word_length):
    words_by_length = []

    import boto3
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

    table = dynamodb.Table('battle_word')
    response = table.query(
        TableName="battle_word",
        KeyConditionExpression="#DDB_word_length = :pkey",
        ExpressionAttributeValues={
            ":pkey": word_length
        },
        ExpressionAttributeNames={
            "#DDB_word_length": "word_length"
        },
    )

    data = response['Items']

    print(data)
    print(len(data))
    return data


#
# def test_grid():
#     gridline = []
#     for i in range(5):
#         gridline.append("")
#     grid = []
#     for i in range(5):
#         grid.append(list(gridline))
#
#     pprint(grid)
#
#
# def test_grid2():
#
#     b = board.Board((12, 12))
#     b.populate("OX  XXOO ")
#     b.draw()


def test_grid(words, grid_size):
    # gridssss = []
    #
    # grids = [["#"] * grid_size for _ in range(grid_size)]
    #
    # for word in words:
    #     gridssss.append([x for x in word['word']])
    #
    # first = words[0]['word']
    #
    # for row in grids:
    #     new_items = [x for x in row]

    random.shuffle(words)
    all_words = [x for x in words[:grid_size]]

    only_words = [word["word"] for word in all_words]

    grid_ok = [list(word) for word in only_words]










    # new_grid = [[x for x in words] for words in grids]
    #
    # grids[0] = [x for x in first]
    #
    # pprint(gridssss)
    # pprint(grids)
    #
    # for row in grids:
    #     print(row)

    pprint(grid_ok)