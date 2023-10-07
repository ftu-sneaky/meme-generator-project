from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class to ingest quotes."""

    formats = ('pdf', 'txt', 'csv', 'docx')

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Validate if file format is supported to ingest quotes."""
        extension = path.split('.')[-1]
        return extension in cls.formats

    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Ingest file in path and return list of quotes."""
        pass