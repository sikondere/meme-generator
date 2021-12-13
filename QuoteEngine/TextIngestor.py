"""TextIngestor."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """TextIngestor."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        with open(path, 'r') as file:
            data = file.readlines()
            for line in data:
                if line != '':
                    parse = line.split('-')
                    quote = QuoteModel(body=parse[0], author=parse[1])
                    quotes.append(quote)
        return quotes
