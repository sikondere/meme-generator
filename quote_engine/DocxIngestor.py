import docx
from typing import List
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text != '':
                parse = paragraph.text.split('-')
                quote = QuoteModel(body = parse[0], author = parse[1])
                quotes.append(quote)
        index = random.randint(0, len(quotes)-1)
        return quotes[index]
