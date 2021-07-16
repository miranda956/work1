import sys
import csv
import requests


def get_next(csv_file):
    with open(csv_file, newline='') as csvfile:
        url_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in url_reader:
            for url in row[0].split(','):
                print(url)
                yield url


def process_url(url):
    page = requests.get(url)
    print(page)


if __name__ == '__main__':
    url_csv_file = sys.argv[3]

    for url in get_next(url_csv_file):
        process_url(url)


