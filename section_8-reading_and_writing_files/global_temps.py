import json
import urllib.request



# json_data_source = 'temperature_anomaly.json'
#
#
# with open(json_data_source,encoding='utf-8') as data:
#     anomalies = json.load(data)
#
# print(anomalies['description'])
# print(anomalies['citation'])
#
# for year,value in anomalies['data'].items():
#     year,value = int(year), float(value)
#     # this is handy to know, within f string round to two deciamls + place values 6 over so all aligned
#     print(f"{year}...{value:6.2f}")
# print('*'*80)



# getting the dat from url
json_data_source = 'https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'

# with open(json_data_source,encoding='utf-8') as data:
# urlopen doesnt let us encode within the func, have to do it explcitly after
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    # using loads not load, load only works with .json files, loads is for loading a string already in python
    # in json format
    anomalies = json.loads(data)


for year,value in anomalies['data'].items():
    year,value = int(year), float(value)
    # this is handy to know, within f string round to two deciamls + place values 6 over so all aligned
    print(f"{year}...{value:6.2f}")
print('*'*80)



