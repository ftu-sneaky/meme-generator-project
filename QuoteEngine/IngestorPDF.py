from .IngestorInterface import IngestorInterface, QuoteModel
from .IngestorTXT import IngestorTXT
import subprocess
import random
import os


class IngestorPDF(IngestorInterface):
    """Quote ingestor class for pdf files."""

    formats = {'pdf'}

    @classmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported the format of the file.')

        temp_file = f"temp_file_{random.randint(0,1000000)}.txt"
        subprocess.run(['pdftotext', path, temp_file])
        quotes = IngestorTXT.parse(temp_file)
        os.remove(temp_file)
        return quotes
