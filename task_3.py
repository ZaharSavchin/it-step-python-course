import csv
from task_2 import MyDialect

with open('data/data.csv', 'w') as file:
    writer = csv.writer(file, dialect=MyDialect)
    writer.writerow(['first', 'second', 'therd'])

    counter = 1
    for i in range(10000):
        writer.writerow([counter, counter, counter])
        counter += 1

def read_csv():
    with open('data/data.csv', 'r') as file:
        quoting = csv.QUOTE_MINIMAL
        reader = csv.DictReader(file,
                                fieldnames=["first", "second", "therd"],
                                quoting=quoting,
                                dialect=MyDialect
                                )
        for i in reader:
            print(i)


read_csv()
