import json
import re


class movieWatchlist():
    def __init__(self, fileName):
        with open(fileName, "r") as file:
            self.data = json.load(file)

    def print(self):
        print("total amount of movies in this list:",
              self.data['movie_watchlist']['total'])
        for key in self.data['titles']:
            print(self.data['titles'][key]["primary"]["title"])


def main():

    # pattern = re.compile("\"tt*\"")
    watchlist = movieWatchlist("data/data.json")
    watchlist.print()


# if this script is ran directly run main
if __name__ == "__main__":
    main()
