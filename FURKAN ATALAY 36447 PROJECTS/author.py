class Author:
    def _init_(self, name, biography):
        self.name = name
        self.biography = biography

    def _str_(self):
        return self.name