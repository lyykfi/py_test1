""" Parse result """

from typing import Sequence

""" class ParserRequestResult """
class ParserRequestResult:
    """ categories collection """
    categories: Sequence[any]

    def __init__(self, categories):
        self.categories = categories
