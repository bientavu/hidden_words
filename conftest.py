import pytest
import requests
from database.dictionary_parser import DictionaryCleaner


@pytest.fixture()
def response():
    return requests.get("https://dictionnaire.lerobert.com/explore/def/X")


@pytest.fixture()
def dict_cleaner():
    dict_cleaner = DictionaryCleaner()
    return dict_cleaner
