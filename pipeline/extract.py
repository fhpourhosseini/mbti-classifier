import csv

def extract(filepath):
    with open(filepath, encoding="cp1252") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            yield row




