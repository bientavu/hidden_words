from decimal import Decimal
from database.db_insertion import db_insertion
from constants import TABLE_NAME
from database.dictionary_parser import WordDownloader, DictionaryCleaner
from app.battle_word import get_words_by_length, GridGenerator

word_downloader = WordDownloader()
dict_cleaner = DictionaryCleaner()

all_words = word_downloader.get_words_list("X")
dicte_def = word_downloader.get_words_definition(all_words)

clean = dict_cleaner.clean(dicte_def)
print(clean)

# db_insertion = db_insertion(clean, TABLE_NAME)

# get_words_by_length = get_words_by_length(10)
# test_grid = test_grid(get_words_by_length, 7)

# grid = GridGenerator(get_words_by_length, 10)
# letter = grid.check_if_letters_are_a_word()
# populate = grid.populate_grid()


# load_data = load_data(12)


