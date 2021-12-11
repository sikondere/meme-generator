from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor

class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in enumerate(cls.ingestors):
            if ingestor.can_ingest(path):
                return ingestor.parse(path)