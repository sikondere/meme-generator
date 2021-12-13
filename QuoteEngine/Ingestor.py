"""Ingestor."""
from typing import List

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
        for _, ingestor in enumerate(cls.ingestors):
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
