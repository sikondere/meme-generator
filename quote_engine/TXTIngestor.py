from typing import List
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        with open(path, 'r') as file:
            data = file.readlines()
            for line in data:
                if line != '':
                    parse = line.text.split('-')
                    quote = QuoteModel(body = parse[0], author = parse[1])
                    quotes.append(quote)
        index = random.randint(0, len(quotes)-1)
        return quotes[index]
