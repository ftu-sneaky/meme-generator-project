from .IngestorInterface import IngestorInterface, QuoteModel


class IngestorTXT(IngestorInterface):
    """Quote ingestor class for txt files."""

    formats = {'txt'}

    @classmethod
    def parse(cls, path: str):
        """Parse txt file and list of QuoteModel."""
        if not cls.can_ingest(path):
            raise Exception('Unsupported the format of the file.')

        quotes = []

        with open(path, 'r') as infile:
            for line in infile:
                content = line.split(' - ')
                if len(content) == 2:
                    body, author = content[0].strip(), content[1].strip()
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)
        return quotes
