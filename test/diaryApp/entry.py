from datetime import datetime


class Entry:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date = datetime.now()

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_body(self, body):
        self.body = body

    def get_body(self):
        return self.body

    def get_diary_details(self):
        return f"{self.get_title()} {self.get_body()}"

    def get_date(self):
        return self.date

    def __eq__(self, other):
        if not isinstance(other, Entry):
            return False
        return (
                self.id == other.id and
                self.title == other.title and
                self.body == other.body and
                self.date == other.date
        )
