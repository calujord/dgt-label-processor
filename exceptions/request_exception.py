class RequestException(Exception):
    message: str

    def __init__(self, message: str):
        """Init request exception."""
        self.message = message
