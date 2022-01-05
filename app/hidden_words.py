import random
import string
from pprint import pprint
import boto3


def get_words_by_length(word_length):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('hidden_words')

    response = table.query(
        TableName="hidden_words",
        KeyConditionExpression="#DDB_key = :pkey",
        ExpressionAttributeValues={
            ":pkey": word_length
        },
        ExpressionAttributeNames={
            "#DDB_key": "key"
        },
    )

    data = response['Items']

    # while 'LastEvaluatedKey' in response:
    #     response = table.query(ExclusiveStartKey=response['LastEvaluatedKey'])
    #     data.extend(response['Items'])

    print(len(data))
    return data


class GridGenerator:
    """
    This class is responsible of generating the grid where
    all the words and the random letters will be inserted.
    """
    def __init__(self, words_number, grid_size):
        """
        Full init of the grid needs. The words from the DB where we take
        some randoms words based on the words number chose by the user.
        And the grid with a grid size chose by the user as well.
        """
        all_database = get_words_by_length(1)
        self.all_words_in_dict = [x for x in all_database]
        self.all_words = [word["word"] for word in self.all_words_in_dict]
        self.random_words = [random.choice(self.all_words)
                             for _ in range(words_number)]
        self.grid_size = grid_size
        self.grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

    def populate_random_words_in_grid(self):
        """
        It will take the grid and try to put the random words one by one.
        It will randomly choose a direction and add each letter of a word,
        by checking if the next letter we add isn't overlapping another
        letter. If it overlaps, it will check if the letters overlapping
        are matching so that the two words can overlap at this very letter.
        """
        orientations = [
            'left-right', 'up-down', 'diagonal-up', 'diagonal-down'
        ]
        for word in self.random_words:
            word_length = len(word)

            placed = False
            while not placed:
                orientation = random.choice(orientations)

                if orientation == 'left-right':
                    x_direction = 0
                    y_direction = 1
                if orientation == 'up-down':
                    x_direction = 1
                    y_direction = 0
                if orientation == 'diagonal-up':
                    x_direction = 1
                    y_direction = 1
                if orientation == 'diagonal-down':
                    y_direction = 1
                    x_direction = -1

                x_position = random.randrange(self.grid_size)
                y_position = random.randrange(self.grid_size)

                ending_x = x_position + word_length * x_direction
                ending_y = y_position + word_length * y_direction

                if ending_x < 0 or ending_x >= self.grid_size:
                    continue
                if ending_y < 0 or ending_y >= self.grid_size:
                    continue

                failed = False

                for i in range(word_length):
                    character = word[i]

                    new_pos_x = x_position + i * x_direction
                    new_pos_y = y_position + i * y_direction

                    character_at_new_pos = self.grid[new_pos_x][new_pos_y]
                    if character_at_new_pos != "_":
                        if character_at_new_pos == character:
                            continue
                        else:
                            failed = True
                            break

                if failed:
                    continue
                else:
                    for i in range(word_length):
                        character = word[i]

                        new_pos_x = x_position + i * x_direction
                        new_pos_y = y_position + i * y_direction

                        self.grid[new_pos_x][new_pos_y] = character
                    placed = True

    def populate_rest_of_grid(self):
        """
        This method will simply add the random letters
        we need to fill the grid, replacing all the '_'.
        """
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.grid[x][y] == '_':
                    self.grid[x][y] = random.choice(string.ascii_uppercase)

    def create_full_grid(self):
        """
        Creating the full grid by calling the two methods.
        """
        self.populate_random_words_in_grid()
        self.populate_rest_of_grid()
        print(self.grid)
        for x in range(self.grid_size):
            print(' '.join(self.grid[x]))

        print('Les mots sont :')
        pprint(self.random_words)

        return self.grid
