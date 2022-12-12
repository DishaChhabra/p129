import pandas as pd
import csv

dataset1 = []
dataset2 = []


with open("Projects/P129/converted_Data.csv", "r") as f:
    for row in csv.reader(f):
        dataset1.append(row)


with open("Projects/P129/bright_stars.csv", "r") as f:
    for row in csv.reader(f):
        dataset2.append(row)


header1 = dataset1[0]
header2 = dataset2[0]

headers = header1 + header2

planet_data1 = dataset1[1:]
planet_data2 = dataset2[1:]

planet_data = []

for i in planet_data1:
    planet_data.append(i)

for j in planet_data2:
    planet_data.append(j)


with open('Projects/P129/finaldata.csv', 'a+') as m:
    writer = csv.writer(m)
    writer.writerow(headers)
    writer.writerows(planet_data)