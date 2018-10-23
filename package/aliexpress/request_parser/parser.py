""" """
import urllib.request
import json_config
import re

from bs4 import BeautifulSoup
from .result import ParserRequestResult
from package.aliexpress.models.category import AliExpressCategory

class AliExpressParserRequest:
    def __init__(self):
        self.config = json_config.connect('./config/request.json')

    def _readHTML(self):
        request = urllib.request.Request(self.config['source_link'])
        response = urllib.request.urlopen(request)
        html = response.read()
        
        return html

    def _parseHTML(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        categories_list_raw = soup.find_all(class_='cate-name')

        return ParserRequestResult(
            map(lambda x: AliExpressCategory(x.text.strip()), categories_list_raw)
        )

    def get_last_data(self):
        html = self._readHTML()
        return self._parseHTML(html)
