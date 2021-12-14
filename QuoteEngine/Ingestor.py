"""Ingestor."""
from typing import List
import sys

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TextIngestor import TextIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Ingestor."""

    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        try:
            for _, ingestor in enumerate(cls.ingestors):
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
        except:
            print('Error: ', sys.exc_info()[0])
