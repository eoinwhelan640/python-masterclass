# rewrite down the python file for invoices
# Doing this because the tab looks wonky on intelliJ, was confirming if i reloaded and resaved it still came out wrong
# It does
import csv

filename = 'invoices.csv'

data=[]
with open(filename, encoding='utf-8',newline='') as readfile:
    reader = csv.reader(readfile, delimiter ='\t')
    for row in reader:
        data.append(row)

# looks ok
print(data)
savefile = 'invoices2.csv'
with open(savefile,'w',encoding='utf-8',newline='') as writefile:
    writer = csv.writer(writefile,delimiter= '\t')
    writer.writerows(data)





