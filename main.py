from decimal import Decimal
from database.db_insertion import db_insertion
from database.dictionary_parser import WordDownloader, DictionaryCleaner
from app.battle_word import get_words_by_length, GridGenerator

# word_downloader = WordDownloader()
# dict_cleaner = DictionaryCleaner()
#
# all_words = word_downloader.get_words_list()
# dicte_def = word_downloader.get_words_definition(all_words)
#
# clean = dict_cleaner.clean(dicte_def)
# print(clean)
#
# app = db_insertion(clean)

get_words_by_length = get_words_by_length(4)
# test_grid = test_grid(get_words_by_length, 7)

grid = GridGenerator(get_words_by_length, 4)
# letter = grid.check_if_letters_are_a_word()
populate = grid.populate_grid()


# load_data = load_data(12)


