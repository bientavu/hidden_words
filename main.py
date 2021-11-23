from database.db_insertion import db_insertion
from database.dictionary_parser import WordDownloader, DictionaryCleaner
from app.battle_word import get_words_by_length
from app.updating_items import update

word_downloader = WordDownloader()
dict_cleaner = DictionaryCleaner()

all_words = word_downloader.get_words_list()
dicte_def = word_downloader.get_words_definition(all_words)

clean = dict_cleaner.clean(dicte_def)
print(clean)

app = db_insertion(clean)

# get_words_by_length = get_words_by_length()
# update = update()
