import csv
import collections
from collections import Counter

with open('data-397-2019-05-16.csv', 'r', encoding='utf-8') as eskalator:
    fields = ["ID","Name","Longitude_WGS84","Latitude_WGS84","NameOfStation","Line","ModeOnEvenDays",
              "ModeOnOddDays","FullFeaturedBPAAmount","LittleFunctionalBPAAmount","BPAAmount",
              "RepairOfEscalators","global_id","geoData"]

    content = csv.DictReader(eskalator, fields, delimiter=',')
    count_eskalator = {}
    for row in content:
        if row['RepairOfEscalators']:
            count_eskalator[row['NameOfStation']] = row['NameOfStation']

    for metro in count_eskalator:
        print(metro)
