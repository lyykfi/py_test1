""" Parse result """

from typing import Sequence
from web.aliexpress.models.category import AliExpressCategory

""" class ParserRequestResult """
class ParserRequestResult:
    """ categories collection """
    categories: Sequence[AliExpressCategory]

    def __init__(self, categories):
        self.categories = categories
