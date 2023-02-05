import csv


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "^"
    quotechar = "+"
    lineterminator = "\n"


csv.register_dialect("new_dialect", dialect=MyDialect)


with open('data/output.csv', 'w') as file:
    writer = csv.writer(file, dialect='new_dialect')
    for i in range(10):
        writer.writerow([i+1, 'hello', 'Hi'])

with open('data/output.csv', 'r') as file:
    reader = csv.reader(file, dialect='new_dialect')

    for row in reader:
        print(row)