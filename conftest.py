import pytest
import requests
from database.dictionary_parser import DictionaryCleaner

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def response():
    return requests.get("https://dictionnaire.lerobert.com/explore/def/X")


@pytest.fixture()
def dict_cleaner():
    dict_cleaner = DictionaryCleaner()
    return dict_cleaner


@pytest.fixture()
def server():
    """Selenium web driver setup"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    selenium = webdriver.Chrome(service=service, options=chrome_options)
    selenium.implicitly_wait(10)
    return selenium

