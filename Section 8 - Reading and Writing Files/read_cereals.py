import csv

filename= 'cereal_grains.csv'

with open(filename,encoding='utf-8',newline='') as csvfile:
    reader = csv.reader(csvfile,quoting = csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)