from test.diaryApp.entry import Entry


class Diary:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.is_locked = True
        self.id_generator = 1
        self.entries = []

    def create_entry(self, title, body):
        entry = Entry(self.generate_id(), title, body)
        self.entries.append(entry)

    def generate_id(self):
        entry_id = self.id_generator
        self.id_generator += 1
        return entry_id

    def find_entry(self, id):
        for entry in self.entries:
            if entry.get_id() == id:
                return entry
        raise Exception(f"Entry with ID {id} not found.")

    def delete_entry(self, id):
        if not self.is_locked:
            entry = self.find_entry(id)
            self.entries.remove(entry)
        else:
            raise Exception("Diary is locked.")

    def update_entry(self, id, title, body):
        if not self.is_locked:
            entry = self.find_entry(id)
            entry.set_title(title)
            entry.set_body(body)

    def get_size(self):
        return len(self.entries)

    def validate_password(self, password):
        if self.password != password:
            raise Exception("Incorrect password.")

    def lock_diary(self):
        self.is_locked = True

    def unlock(self, password):
        self.validate_password(password)
        self.is_locked = False

    def get_user_name(self):
        return self.user_name


