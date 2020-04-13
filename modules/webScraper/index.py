import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from random import randrange


class ScrapProve:
    def __init__(self, base_url, autors_url, table_element):
        self.base_url = base_url
        self.autors_url = autors_url
        self.table_element = table_element

    def get_li_autor(self):
        response = requests.get(self.autors_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Table with autors
        li = soup.find_all('li', class_='list-group-item')
        # Choose random autor html element
        li_autor = li[randrange(self.table_element)]
        return li_autor

    def get_quote_autor(self, href_autor):
        href = self.base_url + href_autor
        response = requests.get(href)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Blockquote with all autor quotes
        blockquote = soup.find_all('blockquote', class_='bsquote')
        element = blockquote[randrange(len(blockquote))]
        return element.p.string
