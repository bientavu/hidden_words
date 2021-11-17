from database.db_insertion import db_insertion
from database.dictionary_parser import WordDownloader, DictionaryCleaner

app = db_insertion()

word_downloader = WordDownloader()
dict_cleaner = DictionaryCleaner()

all_words = word_downloader.get_words_list()
dicte_def = word_downloader.get_words_definition(all_words)

clean = dict_cleaner.clean(dicte_def)
print(clean)