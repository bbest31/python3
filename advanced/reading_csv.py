# Python has a built-in CSV module to read/write CSVs more easily


# reader- lets you iterate over rows of the CSV as lists
# also accepts a delimiter param in case the data isn't seperated by commas - reader(file, delimiter="|")
from csv import reader
with open("podcast_stats.csv") as f:
    csv_reader = reader(f)
    print(csv_reader) # returns the iterator object
    # data = list(csv_reader) - use this line if you want a list of lists
    next(csv_reader)
    # You can also iterate the rows while keeping track of the index
    # for (index, row) in enumerate(csv_reader):
    for episode in csv_reader:
        print(f"{episode[0]} has {episode[1]} downloads, and the last update was {episode[2]}")

# DictReader - lets you iterate over rows of the CSV as OrderedDicts
# The ordered dict makes use of the headers to auto assign keys
from csv import DictReader
with open("podcast_stats.csv") as csv:
    csv_reader = DictReader(csv)
    for row in csv_reader:
        # each row is an OrderedDict
        print(row['Episode'])

# Writing to CSV files

# Using Lists

from csv import writer
with open("podcast_stats2.csv", "w") as f:
    csv_writer = writer(f)
    csv_writer.writerow(["Episode", "Downloads"])
    csv_writer.writerow(["#4 - Neuralink Presentation Commentary", "10000000"])

# Using DictWriter

from csv import DictWriter
with open("podcast_stats2.csv","w") as csv:
    headers = ["Episode", "Downloads", "Date"]
    csv_writer = DictWriter(csv, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Episode" : "#5 - Episode 5",
        "Downloads" : 123,
        "Date" : "2020-04-11"
    })