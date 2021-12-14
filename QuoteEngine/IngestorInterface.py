"""Ingestor Interface."""
from abc import ABC, abstractmethod
from typing import List
import sys

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Ingestor Interface."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Found the method can_ingest."""
        try:
            extension = path.split('.')[-1]
            return extension in cls.allowed_extensions
        except:
            print('Error: ', sys.exc_info()[0])

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        pass
