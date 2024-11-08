from datetime import datetime


class Note:
    def __init__(self, author, title, text, tags=None):
        self.author = author
        self.title = title
        self.text = text
        self.created = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.tags = tags if tags else "N/A"

    def __str__(self):
        return f"{self.author} - {self.title}: {self.text}"
