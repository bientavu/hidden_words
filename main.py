from app.pdf_generator import PdfGenerator

# word_downloader = WordDownloader()
# dict_cleaner = DictionaryCleaner()
#
# all_words = word_downloader.get_words_list("X")
# dicte_def = word_downloader.get_words_definition(all_words)
#
# clean = dict_cleaner.clean(dicte_def)
# print(clean)

# db_insertion = db_insertion(clean, TABLE_NAME)

# get_words_by_length = get_words_by_length(8)
# get_all_words = get_all_words()
# test_grid = test_grid(get_words_by_length, 7)

# grid = GridGenerator(get_words_by_length, 8)
# letter = grid.check_if_letters_are_a_word()
# populate = grid.generate_grid()
# line_length = grid.check_line_length(populate)


# load_data = load_data(12)


# hidden_words = GridGenerator(8, 20)
# hidden_words.create_full_grid()
# test = hidden_words.random_words
# print(test)

pdf_generator = PdfGenerator(12, 24)
create_pdf = pdf_generator.generate_pdf()
