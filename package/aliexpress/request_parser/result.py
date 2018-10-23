""" """
import urllib.request
import json_config

from typing import Sequence
from package.aliexpress.models.category import AliExpressCategory

class ParserRequestResult:
    categories: Sequence[AliExpressCategory]

    def __init__(self, categories):
        self.categories = categories
