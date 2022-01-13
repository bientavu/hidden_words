from constants import TABLE_NAME, ALL_LETTERS
from database.dictionary_parser import WordDownloader, DictionaryCleaner
from database.db_insertion import db_insertion

word_downloader = WordDownloader()
dictionary_cleaner = DictionaryCleaner()

all_words = word_downloader.get_words_list(ALL_LETTERS)
all_words_and_def = word_downloader.get_words_definition(all_words)

clean = dictionary_cleaner.clean(all_words_and_def)
db_insertion = db_insertion(clean, TABLE_NAME)
