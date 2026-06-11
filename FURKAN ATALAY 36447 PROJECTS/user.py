class User:
    def _init_(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def _str_(self):
        return f"User: {self.name} (ID: {self.user_id})"