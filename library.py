import json
import random


class Library:
    def __init__(self, database: list):
        self.data = database

    def info(self, title: str) -> None:
        counter = 0
        for i in range(len(self.data)):
            if (self.data[i]["Title"] == title) and\
               (self.data[i]["Type"] == 'movie'):
                print("{} ({})".format(self.data[i]["Title"],
                                       self.data[i]["Year"]))
                counter += 1
                break
            elif (self.data[i]["Title"] == title) and\
                 (self.data[i]["Type"] == 'series'):
                try:
                    series = [i for i in self.data if i["Type"] == 'series']
                    season = max([i['Season'] for i in series
                                  if i['Title'] == title])
                    episode = max([i['Episode'] for i in series
                                   if (i['Title'] == title) and
                                   (i['Season'] == season)])
                    print("{} S{:02d}E{:02d}".format(title, season, episode))
                    counter += 1
                    break
                except Exception:
                    pass
        if counter == 0:
            print("Podany przez Ciebie tytuł nie znajduje się w naszej bazie.")

    def search(self, title: str) -> dict:
        return json.dumps([i for i in self.data if i["Title"] == title],
                          indent=4)

    def __repr__(self) -> str:
        text = ''
        for i in self.data:
            text += json.dumps(i, indent=4)
        return text

    def play(self, title: str, season: int = None, episode: int = None) -> None:
        for i in range(len(self.data)):
            if self.data[i]["Type"] == 'movie':
                if self.data[i]["Title"] == title:
                    self.data[i]["ViewCount"] = self.data[i]["ViewCount"] + 1
            elif self.data[i]["Type"] == 'series':
                if (self.data[i]["Title"] == title) and\
                   (self.data[i]["Season"] == season) and\
                   (self.data[i]["Episode"] == episode):
                    self.data[i]["ViewCount"] = self.data[i]["ViewCount"] + 1

    def get_movies(self) -> list:
        movies = [i for i in self.data if i["Type"] == 'movie']
        return sorted(movies, key=lambda x: x['Title'])

    def get_series(self) -> list:
        series = [i for i in self.data if i["Type"] == 'series']
        return sorted(series, key=lambda x: (x['Title'], x['Season'],
                                             x['Episode']))

    def generate_views(self):
        if len(self.data) == 0:
            print("Your database is empty!")
        else:
            random_number = random.randint(0, len(self.data)-1)
            self.data[random_number]["ViewCount"] = random.randint(1, 100)

    def ten_generations(self):
        for _ in range(10):
            self.generate_views()

    def top_titles(self, content_type: str = None) -> list:
        num = 3
        if content_type in ['movie', 'series']:
            data = [i for i in self.data if i["Type"] == content_type]
        else:
            data = self.data
        top = sorted(data, key=lambda x: x['ViewCount'], reverse=True)
        top_num = []
        for i in top:
            if not i['Title'] in top_num:
                top_num.append(i['Title'])

        return top_num[:num]

    def add_season(self, title: str, year: int, genre: str,
                   season: int, episodes: int):
        for i in range(episodes):
            _data = {
                'Type': 'series', 'Title': title, 'Year': year,
                'Genre': genre, 'Season': season, 'Episode': i+1,
                'ViewCount': 0}
            self.data.append(_data)

    def add_movie(self, title: str, year: int, genre: str):
        _data = {
            'Type': 'movie', 'Title': title, 'Year': year,
            'Genre': genre, 'ViewCount': 0}
        self.data.append(_data)


database = [
    {'Type': 'movie', 'Title': 'The Matrix', 'Year': 1999,
     'Genre': 'Action', 'ViewCount': 0},
    {'Type': 'movie', 'Title': 'The Godfather', 'Year': 1972,
     'Genre': 'Drama', 'ViewCount': 0},
    {'Type': 'movie', 'Title': 'Interstellar', 'Year': 2014,
     'Genre': 'Science-Ficton', 'ViewCount': 0},
    {'Type': 'series', 'Title': 'Vikings', 'Year': 2013,
     'Genre': 'Action', 'Season': 1, 'Episode': 1, 'ViewCount': 0},
    {'Type': 'series', 'Title': 'Vikings', 'Year': 2013,
     'Genre': 'Action', 'Season': 1, 'Episode': 2, 'ViewCount': 0},
    {'Type': 'series', 'Title': 'Peaky Blinders', 'Year': 2013,
     'Genre': 'Action', 'Season': 1, 'Episode': 1, 'ViewCount': 0},
    {'Type': 'series', 'Title': 'Peaky Blinders', 'Year': 2013,
     'Genre': 'Action', 'Season': 1, 'Episode': 2, 'ViewCount': 0},
    {'Type': 'series', 'Title': 'Gomorra: La serie', 'Year': 2014,
     'Genre': 'Criminal', 'Season': 1, 'Episode': 1, 'ViewCount': 0},
    {'Type': 'series', 'Title': 'Gomorra: La serie', 'Year': 2014,
     'Genre': 'Criminal', 'Season': 1, 'Episode': 2, 'ViewCount': 0},
]

db = []


if __name__ == "__main__":
    lib = Library(db)
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
    print(lib.search("Gomorra: La serie"))
    for _ in range(1000):
        lib.ten_generations()
    print(lib.search("Gomorra: La serie"))
    print(lib.top_titles('series'))
    series_counter(lib, 'Peaky Blinders')
