"""PDFIngestor."""
import subprocess
import os
from typing import List
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDFIngestor."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        tmp = f'./tmp_{random.randint(0, 10000)}.txt'
        subprocess.call(['pdftotext', path, tmp])
        with open(tmp, 'r') as file:
            quotes = []
            for line in file.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(body=parse[0], author=parse[1])
                quotes.append(quote)
        os.remove(tmp)
        return quotes
