from library import Library
from datetime import datetime


def series_counter(library: object, title: str):
    """Print sum of episodes in all series."""
    x = len([i for i in library.data if i["Title"] == title])
    print(x)


db = []


if __name__ == "__main__":
    print('Biblioteka filmów')
    lib = Library(db)
    lib.add_season("Vikings", 2014, "Adventure", 1, 12)
    lib.add_season("Vikings", 2015, "Adventure", 2, 12)
    lib.add_season("Vikings", 2016, "Adventure", 3, 12)
    lib.add_season("Vikings", 2016, "Adventure", 4, 12)
    lib.add_season("Gomorra: La serie", 2014, "Criminal", 1, 12)
    lib.add_season("Gomorra: La serie", 2015, "Criminal", 2, 12)
    lib.add_season("Gomorra: La serie", 2017, "Criminal", 3, 10)
    lib.add_season("Peaky Blinders", 2013, "Drama", 1, 10)
    lib.add_season("Peaky Blinders", 2014, "Drama", 2, 12)
    lib.add_season("Peaky Blinders", 2014, "Drama", 3, 12)
    lib.add_season("Peaky Blinders", 2015, "Drama", 4, 8)
    lib.add_movie("The Godfather", 1979, "Drama")
    lib.add_movie("Interstellar", 2014, "Science-Fiction")
    lib.add_movie("The Matrix", 1999, "Action")
    for _ in range(1000):
        lib.ten_generations()
    print("Najpopularniejsze filmy i seriale dnia {} to:"
          .format(datetime.today().date().strftime('%d-%m-%Y')))
    for i in lib.top_titles():
        print(i)
