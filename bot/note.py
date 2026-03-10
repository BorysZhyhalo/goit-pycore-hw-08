from datetime import datetime


class Note:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.tags = []

    def __str__(self):
        return f"[{self.title}] {self.body}"
