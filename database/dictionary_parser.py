import string
import unicodedata
import unidecode
import requests
from bs4 import BeautifulSoup
from constants import WORD_LIST_URL, GET_DEF_URL


class WordDownloader:
    """
    Class that will parse the online web word dictionary.
    It takes all the words from A to Z.
    Then takes all the definitions from the taken words.
    """

    @staticmethod
    def get_words_list():
        """
        Gets all the words from A to Z. As there is multiple pages,
        we need to scrape all of them as well. We make sure to break
        when we reached the final page of the actual letter.
        """
        letters = list(string.ascii_uppercase)
        all_words = []

        for letter in letters:
            page = 1
            while page != 100:
                url = WORD_LIST_URL + f'{letter}/{page}'
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
        """
        It adds the word and his definition we scraped
        (added in the actual dictionary) into the main list.
        """
        denormalized_word = soup.find('h1').text
        denormalized_def = word_def.text
        this_dict['word'] = unicodedata.normalize(
            "NFKC",
            denormalized_word
        )
        this_dict['definition'] = unicodedata.normalize(
            "NFKC",
            denormalized_def
        )
        all_words_and_def.append(this_dict)

    def get_words_definition(self, all_words):
        """
        Method that run through all HTML words pages in order to
        get their definitions. Multiple HTML levels are looked so
        that we take the proper definition (sometimes the first def
        of a list, sometimes another type of def, etc).
        """
        all_words_and_def = []

        for word in all_words:
            url = GET_DEF_URL + word
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
    """
    Cleans the list of dictionaries before
    adding them to the Dynamo DB.
    """
    @staticmethod
    def remove_all_accents_from_words(dictionary):
        dictionary["word"] = unidecode.unidecode(dictionary["word"])

        # dictionary["word"] = dictionary["word"].replace("é", "e")

    @staticmethod
    def all_words_in_uppercase(dictionary):
        """
        All words letters are put in uppercase so that we can
        directly show them in uppercase inside the solution PDF.
        """
        dictionary["word"] = dictionary["word"].upper()

    @staticmethod
    def replace_audio_error(dictionary):
        """
        Removes this extra text that appears when there is
        an audio plugin inside the definition we scrape.
        """
        text = "\n\n\n\u200b\u200b\u200b\n          \n\n\n\n\n\n\n\n\n" \
               "Votre navigateur ne prend pas en charge audio.\n\n\n"

        dictionary["definition"] = dictionary["definition"].replace(text, "")

    @staticmethod
    def remove_words_that_starts_with_a_star(dictionary):
        """
        Removes the * for some words that
        have it at the beginning of the word.
        """
        dictionary["word"] = dictionary["word"].replace("*", "")

    @staticmethod
    def add_words_length_to_dict(dictionary):
        """
        Add the words length to the dictionaries so that
        we can better and faster scan our Dynamo DB.
        """
        dictionary['word_length'] = len(dictionary['word'])

    def clean(self, words_dict):
        """
        Operates the cleaning.
        """
        for dictionary in words_dict:
            self.remove_all_accents_from_words(dictionary)
            self.all_words_in_uppercase(dictionary)
            self.replace_audio_error(dictionary)
            self.remove_words_that_starts_with_a_star(dictionary)
            self.add_words_length_to_dict(dictionary)

        return words_dict
