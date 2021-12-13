"""QuoteModel."""


class QuoteModel:
    """QuoteModel."""

    def __init__(self, body: str, author: str) -> None:
        """Found the Initialization method."""
        self.body = body
        self.author = author

        def __repr__(self):
            """Found the repr."""
            return f'body: {self.body}, author: {self.author}'

        def __str__(self):
            """Found the str method."""
            return f'body: {self.body}, author: {self.author}'
