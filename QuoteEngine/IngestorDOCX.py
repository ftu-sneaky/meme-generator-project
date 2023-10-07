from .IngestorInterface import IngestorInterface, QuoteModel
from docx import Document


class IngestorDOCX(IngestorInterface):
    """Quote ingestor class for csv files."""

    formats = {'docx'}

    @classmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported the format of the file.')
        content = Document(path)
        quotes = []
        for line in content.paragraphs:
            words = line.text.split(' - ')
            if len(words) == 2:
                quote = QuoteModel(words[0], words[1])
                quotes.append(quote)
        return quotes
