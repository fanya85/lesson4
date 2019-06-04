import csv
import geopy
from geopy.distance import geodesic


result = {}
with open('data-397-2019-05-16.csv', 'r', encoding='utf-8') as f:
    metro_reader = csv.DictReader(f, delimiter=",")
    for row in metro_reader:
        pt1 = geopy.Point(row['Longitude_WGS84'], row['Latitude_WGS84'])
        with open("file.csv", 'r', encoding='ANSI') as ff:
            bus_reader = csv.DictReader(ff, delimiter=";")
            for i in bus_reader:
                try:
                    pt2 = geopy.Point(i["Longitude_WGS84"], i["Latitude_WGS84"])
                except ValueError:
                    continue

                dist = geopy.distance.distance(pt1, pt2).km

                if dist <= 0.5:
                    if row['Name'] in result:
                        result[row['Name']] += 1

                    else:
                        result[row['Name']] = 1

    print(sorted(result.items(), key=lambda item: item[1], reverse=True)[0][0])
