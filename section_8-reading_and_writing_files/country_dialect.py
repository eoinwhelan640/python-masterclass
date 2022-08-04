import csv
filename='country_info.txt'

# not really efficient way to do it, read whole thing, sniff, then restart whole file
# with open(filename,encoding='utf-8',newline='') as countries_data:
#     sample = countries_data.read()
#     country_dialect = csv.Sniffer().sniff(sample)
#     countries_data.seek(0)
#     country_reader = csv.reader(countries_data, dialect=country_dialect)
#     for row in country_reader:
#         print(row)

# Instead, read first few lines, sniff that and then restart
with open(filename,encoding='utf-8',newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.read()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*'*80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace'
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect,attribute))}')