class QuoteModel:
    """Class for a quote to encapsulate the body and author."""

    def __init__(self, body, author):
        """Initialize body and author properties."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return string representation of quote."""
        return f'<{self.body}, {self.author}>'
