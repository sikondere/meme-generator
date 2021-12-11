import pandas as pd
from typing import List
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        df = pd.read_csv(path, header = 0)
        for index, row in df.iterrows():
            quote = QuoteModel(body = row['body'], author = row['author'])
            quotes.append(quote)
        index = random.randint(0, len(quotes)-1)
        return quotes[index]
