from bs4 import BeautifulSoup
from database.dictionary_parser import WordDownloader, DictionaryCleaner


class TestWordDownloader:
    """
    Class that performs different tests for the WordDownloader
    """
    def test_alive(self, response):
        """
        Check if status code is OK (200)
        """
        assert response.status_code == 200

    def test_html_title(self, response):
        """
        Check generally the HTML, here we check the page title
        """
        soup = BeautifulSoup(response.content, "lxml")

        assert soup.title.text == "Mots commençant par X | " \
                                  "Dico en ligne Le Robert"

    def test_find_words_in_page(self, response):
        """
        We check if we find the same words
        """
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
        """
        We test is the cleaning method is working (also adding
        key/value pair).
        """
        entry = [
            {'word': '*Héllo', 'definition': 'Dire bonjour'}
        ]
        expected_result = [
            {'word': 'HELLO', 'definition': 'Dire bonjour', 'key': 1}
        ]
        dict_cleaner = DictionaryCleaner()
        result = dict_cleaner.clean(entry)

        assert result == expected_result
