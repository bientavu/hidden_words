from database.db_insertion import db_insertion
from database.dictionary_parser import WordDownloader, DictionaryCleaner

word_downloader = WordDownloader()
dict_cleaner = DictionaryCleaner()

all_words = word_downloader.get_words_list()
dicte_def = word_downloader.get_words_definition(all_words)

clean = dict_cleaner.clean(dicte_def)
print(clean)

app = db_insertion(clean)
