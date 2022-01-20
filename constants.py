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

# Sentry
DSN = "https://2bd5743c0fef417aa2423829130ff6dc@o1035883.ingest.sentry.io" \
      "/6157001 "
