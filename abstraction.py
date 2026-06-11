from abc import ABC, abstractmethod

class Movie(ABC):

    @abstractmethod
    def show_details(self):
        pass


class ActionMovie(Movie):
    def show_details(self):
        print("Title: Fast Action")
        print("Genre: Action")


movie = ActionMovie()
movie.show_details()
