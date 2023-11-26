import json
import random


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

    def get_movies(self):
        movies = [i for i in self.data if i["Type"] == 'movie']
        return sorted(movies, key=lambda x: x['Title'])

    def get_series(self):
        series = [i for i in self.data if i["Type"] == 'series']
        return sorted(series, key=lambda x: (x['Title'], x['Season'],
                                             x['Episode']))

    def generate_views(self):
        random_number = random.randint(0, len(self.data)-1)
        self.data[random_number]["ViewCount"] = random.randint(1, 100)

    def ten_generatations(self):
        for i in range(10):
            self.generate_views()

    def top_titles(self, content_type=None):
        num = 3
        if content_type in ['movie', 'series']:
            data = [i for i in self.data if i["Type"] == content_type]
        else:
            data = self.data
        return sorted(data, key=lambda x: x['ViewCount'], reverse=True)[:num]


if __name__ == "__main__":
    lib = Library(database)
    print(lib.search("Gomorra: La serie"))
    lib.info("Gomorra: La serie")
    lib.ten_generatations()
    print(lib.top_titles('movie'))
