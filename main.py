import json


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


if __name__ == "__main__":
    lib = Library(database)
    print(lib.search("Gomorra: La serie"))
    lib.info("Gomorra: La serie")
