import csv

filename = 'OlympicMedals_2020.csv'

# with open(filename, encoding='utf-8', newline='') as csvfile:
#     text = csv.reader(csvfile)
#     headings = next(text)
#     #out = dict.fromkeys([h.casefold() for h in headings])
#     output = {}
#     for rank,country,gold,silver,bronze,total in text:
#         out = {}
#         #print(rank,country,gold,silver,bronze,total)
#         out['rank'] = rank
#         out['gold'] = gold
#         out['silver'] = silver
#         out['bronze'] = bronze
#         out['total'] = total
#         output[country] = out
#
# # How to align it - my way
# for country,stats in output.items():
#     print(f'{f"[{country}]":<20} {f"{stats}":<75} {country:<20}')

with open(filename, encoding='utf-8', newline='') as csvfile:
    headers = csvfile.readline().strip('\n').split(',')
    print(f'Column headers: {headers}')
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)