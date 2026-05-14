class Movie:
    def __init__(self, rating, genre):
        self.rating = rating
        self.genre = genre

rush_hour = Movie(8.9, "Action comedy")

print(rush_hour.rating)
print(rush_hour.genre)