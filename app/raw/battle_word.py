from pprint import pprint
from itertools import product
import random
import boto3
import numpy
from constants import TABLE_NAME
from boto3.dynamodb.conditions import Key, Attr


def get_words_by_length(word_length):
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

def get_all_words():
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('battle_word')
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    print(data)
    print(len(data))

class GridGenerator:
    def __init__(self, words, grid_size):
        self.words = words
        self.grid_size = grid_size
        random.shuffle(self.words)
        self.all_words = [x for x in words]
        # self.only_words = [word["word"] for word in self.all_words]
        self.only_words = [
            list(word) for word in [word["word"] for word in self.all_words]
        ]
        self.empty_grid = [['-'] * self.grid_size for _ in
                           range(self.grid_size)]
        self.word_position = self.empty_grid[0]

    def check_if_letters_are_a_word(self):
        pass
        # self.x = 0
        # self.y = 0
        # for letter in self.only_words
        # if self.only_words[:self.grid_size][self.y] +
        # for word, pos in zip(self.only_words[:self.grid_size], range(self.grid_size)):
        #     for letter in word:
        #         if letter[range(self.grid_size)]
        #         self.empty_grid[pos] = word
        # pprint(self.empty_grid)

    def populate_grid(self):
        # for word in self.only_words[:self.grid_size]:
        #     for pos in range(self.grid_size):
        #         self.empty_grid[pos] = word
        # pprint(self.empty_grid)
        first = True
        # detect = []
        for word, pos in zip(self.only_words,
                             range(len(self.only_words))):
            if first:
                first = False
                self.empty_grid[pos] = word
                pprint(self.empty_grid)
            else:
                detect = []
                for indice, letter in enumerate(list(word)):
                    search = ""
                    for word_list in self.empty_grid:
                        if word_list[indice] != '#':
                            search += word_list[indice]
                    print(search)
                    detect = [w['word'] for w in self.words if w['word'].startswith(search + letter)]
                    if not detect:
                        break
                if not detect:
                    continue
            self.empty_grid[pos] = word
            pprint(self.empty_grid)


    def populate_grid_2(self):
        # for word in self.only_words[:self.grid_size]:
        #     for pos in range(self.grid_size):
        #         self.empty_grid[pos] = word
        # pprint(self.empty_grid)
        first = True
        next_position = 0
        # detect = []
        for word, pos in zip(self.only_words,
                             range(len(self.only_words))):
            if first:
                first = False
                self.empty_grid[0] = word
            else:
                detect = []
                for indice, letter in enumerate(list(word)):
                    search = ""
                    for word_list in self.empty_grid:
                        if word_list[indice] != '#':
                            search += word_list[indice]

                    detect = [w['word'] for w in self.words if w['word'].startswith(search + letter)]
                    if not detect:
                        break
                if not detect:
                    continue
            self.empty_grid[next_position] = word
            next_position += 1
        pprint(self.empty_grid)


    def generate_grid(self):

        coord = list(product(range(self.grid_size), range(self.grid_size)))
        for bloc in random.sample(coord, 8):
            self.empty_grid[bloc[0]][bloc[1]] = '#'

        pprint(self.empty_grid)

        for row in self.empty_grid:
            print(' '.join(row))

        return self.empty_grid


    def check_line_length(self, empty_grid):
        length = 0
        lengthh = {}

        for line in empty_grid:
            for i in line:
                if i == "-":
                    length += 1
                else:
                    pass

            print(length)