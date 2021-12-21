import boto3# word_downloader = WordDownloader()
# dict_cleaner = DictionaryCleaner()
#
# all_words = word_downloader.get_words_list()
# dicte_def = word_downloader.get_words_definition(all_words)
#
# clean = dict_cleaner.clean(dicte_def)
# print(clean)


def db_insertion(words_dict, table_name):
    """
    Inserts all the dictionaries collected by the dictionary parser
    into the DynamoDB table. Table_name can be updated in the
    constant.py module. The insertion may take some times, it's
    because the scraping is time consuming.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    with table.batch_writer() as batch:
        for dictionary in words_dict:
            batch.put_item(
                Item={
                    'word': dictionary['word'],
                    'definition': dictionary['definition'],
                    'key': dictionary['key']
                }
            )
