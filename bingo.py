import csv

with open('citation.csv', 'rb') as csvfile:
    data = list(csv.reader(csvfile))

datacon = [[row[0],int(row[1])] for row in data]

hindexlist = []
datc = 0
hindex = 0
count = 0
name=datacon[0][0]
for datum in datacon:
    if datum[0] != name:
        row = [name, hindex]
        hindexlist.append(row)
        hindex = 0
        count = 0
        name = datum[0]
    count = count + 1
    if count <= datum[1]:
        hindex = hindex + 1
        continue
hindexlist = [[row[0],str(row[1])] for row in hindexlist]
with open('hindex.csv', 'wr') as hindexfile:
    writer = csv.writer(hindexfile)
    writer.writerows(hindexlist)
