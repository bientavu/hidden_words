from bs4 import BeautifulSoup
from database.dictionary_parser import WordDownloader, DictionaryCleaner
import pytest
import requests


class TestWordDownloader:
    def test_alive(self, response):
        assert response.status_code == 200

    def test_html_title(self, response):
        soup = BeautifulSoup(response.content, "lxml")

        assert soup.title.text == "Mots commençant par X | " \
                                  "Dico en ligne Le Robert"

    def test_find_words_in_page(self, response):
        word_downloader = WordDownloader()
        all_words_actual = word_downloader.get_words_list("X")
        all_words_expected = []
        soup = BeautifulSoup(response.content, "lxml")
        data = soup.find(class_='l-l')
        for word in data.find_all('a'):
            all_words_expected.append(word['href'])

        assert all_words_expected is not None
        assert all_words_actual == all_words_expected


class TestDictionaryCleaner:
    def test_clean(self):
        entry = [
            {'word': '*Héllo', 'definition': 'Dire bonjour'}
        ]
        expected_result = [
            {'word': 'HELLO', 'definition': 'Dire bonjour', 'word_length': 5}
        ]
        dict_cleaner = DictionaryCleaner()
        result = dict_cleaner.clean(entry)

        assert result == expected_result
