import csv
filename = 'cereal_grains.csv'

with open(filename,encoding='utf-8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

print(reader)



input_filename = 'country_info.txt'
dialect = csv.excel
dialect.delimiter = '|'


countries = {}
with open(input_filename,encoding='utf-8',newline='') as country_file:
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    # good way to change the headings, read first line and convert it all with casefold()
    # for index,heading in enumerate(headings):
    #     headings[index] = heading.casefold()
    headings = [h.casefold() for h in headings]
    reader = csv.DictReader(country_file, delimiter='|',dialect=dialect,fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row


print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif country_key == 'quit':
        break
