import string

# Dictionary parser
WORD_LIST_URL = "https://dictionnaire.lerobert.com/explore/def/"
GET_DEF_URL = "https://dictionnaire.lerobert.com"

# Db insertion
TABLE_NAME = "hidden_word"
ALL_LETTERS = list(string.ascii_uppercase)

# S3
BUCKET_NAME = "hidden-words-resources"
OBJECT_KEY = "pdf"
