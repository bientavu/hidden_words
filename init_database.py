from constants import TABLE_NAME, ALL_LETTERS
from database.dictionary_parser import WordDownloader, DictionaryCleaner
from database.db_insertion import db_insertion

word_downloader = WordDownloader()
dictionary_cleaner = DictionaryCleaner()

print("Scraping all the words...")
all_words = word_downloader.get_words_list(ALL_LETTERS)

print("Scraping all the words definitions...")
all_words_and_def = word_downloader.get_words_definition(all_words)

print("Cleaning all the words...")
clean = dictionary_cleaner.clean(all_words_and_def)

print("Inserting all the words in the DB...")
db_insertion = db_insertion(clean, TABLE_NAME)
