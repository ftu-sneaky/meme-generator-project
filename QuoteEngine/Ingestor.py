from .IngestorCSV import IngestorCSV
from .IngestorDOCX import IngestorDOCX
from .IngestorInterface import IngestorInterface
from .IngestorPDF import IngestorPDF
from .IngestorTXT import IngestorTXT


class Ingestor(IngestorInterface):
    """Encapsulate corresponding quote ingestor based on it's file type."""

    available_ingestors = {IngestorCSV, IngestorDOCX, IngestorPDF, IngestorTXT}

    @classmethod
    def parse(cls, path):
        """Ingest the file with appropriate ingestor."""
        for ingestor in cls.available_ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
