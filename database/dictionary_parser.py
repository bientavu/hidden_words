import string
import unicodedata
import requests
from bs4 import BeautifulSoup


class WordDownloader:

    @staticmethod
    def get_words_list():
        letters = list(string.ascii_uppercase)
        all_words = []

        for letter in letters:
            page = 1
            while page != 100:
                url = f'https://dictionnaire.lerobert.com/explore/def/' \
                      f'{letter}/{page}'
                soup = BeautifulSoup(requests.get(url=url).text, 'lxml')
                data = soup.find(class_='l-l')
                if 'Aucun résultat trouvé' in data.text:
                    break
                for word in data.find_all('a'):
                    all_words.append(word['href'])
                page = page + 1

        print(all_words)
        print(len(all_words))
        return all_words

    @staticmethod
    def add_to_dictionary(all_words_and_def, soup, this_dict, word_def):
        denormalized_word = soup.find('h1').text
        denormalized_def = word_def.text
        this_dict['word'] = unicodedata.normalize(
            "NFKD",
            denormalized_word
        )
        this_dict['definition'] = unicodedata.normalize(
            "NFKD",
            denormalized_def
        )
        all_words_and_def.append(this_dict)

    def get_words_definition(self, all_words):
        base_url = 'https://dictionnaire.lerobert.com'
        all_words_and_def = []

        for word in all_words:
            url = base_url + word
            this_dict = {}
            soup = BeautifulSoup(requests.get(url=url).text, 'html.parser')
            if soup.find_all(class_='d_dvn'):
                first_def = soup.find(class_='d_dvn')
                word_def = first_def.find(class_='d_dfn')
                if word_def is None:
                    word_def = first_def.find(class_='d_gls')
                    if word_def is None:
                        continue
                self.add_to_dictionary(all_words_and_def, soup, this_dict,
                                       word_def)
            else:
                word_def = soup.find(class_='d_dfn')
                if word_def is None:
                    word_def = soup.find(class_='d_gls')
                    if word_def is None:
                        continue
                self.add_to_dictionary(all_words_and_def, soup, this_dict,
                                       word_def)

        return all_words_and_def


class DictionaryCleaner:

    @staticmethod
    def all_words_in_uppercase(words_dict):
        """All letters are put in uppercase"""
        words_dict["word"] = words_dict["word"].upper()

        return words_dict

    @staticmethod
    def replace_audio_error(words_dict):
        text = "\n\n\n\u200b\u200b\u200b\n          \n\n\n\n\n\n\n\n\n" \
              "Votre navigateur ne prend pas en charge audio.\n\n\n"

        words_dict["definition"] = words_dict["definition"].replace(text, "")

        return words_dict

    def clean(self, words_dict):
        for dictionary in words_dict:
            self.all_words_in_uppercase(dictionary)
            self.replace_audio_error(dictionary)

        return words_dict
