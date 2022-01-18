from app.hidden_words import GridGenerator
from app.pdf_generator import PdfGenerator
from constants import TABLE_NAME, ALL_LETTERS
from database.dictionary_parser import WordDownloader, DictionaryCleaner
from database.db_insertion import db_insertion

word_downloader = WordDownloader()
dict_cleaner = DictionaryCleaner()

print("Scraping all the words...")
all_words = word_downloader.get_words_list("X")
print("Scraping all the words definitions...")
dicte_def = word_downloader.get_words_definition(all_words)

print("Cleaning all the words...")
clean = dict_cleaner.clean(dicte_def)
# print(clean)
# print(len(clean))

# db_insertion = db_insertion(clean, TABLE_NAME)

# get_words_by_length = get_words_by_length(8)
# get_all_words = get_all_words()
# test_grid = test_grid(get_words_by_length, 7)

# grid = GridGenerator(get_words_by_length, 8)
# letter = grid.check_if_letters_are_a_word()
# populate = grid.generate_grid()
# line_length = grid.check_line_length(populate)
# load_data = load_data(12)

# hidden_words = GridGenerator(10, 16)
# hidden_words.create_full_grid()

# pdf_generator = PdfGenerator(10, 17)
# create_pdf = pdf_generator.generate_pdf()
# test = hidden_words.random_words
# print(test)
