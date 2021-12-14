"""Docx Ingestor."""
import docx
from typing import List
import sys

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Docx Ingestor."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest exception')
            quotes = []
            doc = docx.Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text != '':
                    parse = paragraph.text.split('-')
                    quote = QuoteModel(body=parse[0], author=parse[1])
                    quotes.append(quote)
            return quotes
        except:
            print('Error: ', sys.exc_info()[0])
