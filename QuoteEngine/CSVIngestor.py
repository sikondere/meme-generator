"""CSV ingestor."""
import pandas as pd
from typing import List
import sys

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """CSV ingestor."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest exception')
            quotes = []
            df = pd.read_csv(path, header=0)
            for index, row in df.iterrows():
                quote = QuoteModel(body=row['body'], author=row['author'])
                quotes.append(quote)
            return quotes
        except:
            print('Error: ', sys.exc_info()[0])
