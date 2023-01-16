# import time
#
# start_time = time.time()
# for i in range(1_000_000):
#     j = i * i
# end_time = time.time()
# print(end_time-start_time)
import random


class Movie:

    def __init__(self, name, duration_in_min, genre, **kwargs):
        self.id = random.randint()
        self.genre = genre
        self.duration_in_min = duration_in_min
        self.name = name
        # director = "Steven Spielberg"
        # kwargs = {'director': "Steven Spielberg"}
        for k, v in kwargs.items():
            self.__setattr__(k, v)


class CinemaBranch:

    def __init__(self, name, city, address, phone):
        self.id = random.randint()
        self.phone = phone
        self.address = address
        self.city = city
        self.name = name


class Cinema:

    def __init__(self, name):
        self.name = name
        self.branches: set[CinemaBranch] = set()
        self.movies: dict[str, Movie] = {}

    def add_movie(self, movie: Movie):
        # add validations?
        self.movies[movie.name] = movie

    def get_movie_by_name(self, name) -> Movie | None:
        # validations
        return self.movies.get(name)

    # def add_movie(self, name, duration_in_min, ):
    #     pass



