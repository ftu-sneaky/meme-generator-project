from .IngestorInterface import IngestorInterface, QuoteModel
import csv


class IngestorCSV(IngestorInterface):
    """Quote ingestor class for csv files."""

    formats = {'csv'}

    @classmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported the format of the file.')
        quotes = []
        with open(path, 'r') as infile:
            content = csv.reader(infile)
            next(content, None)
            for row in content:
                quote = QuoteModel(row[0], row[1])
                quotes.append(quote)
        return quotes
