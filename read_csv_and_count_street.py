import csv
import collections
from collections import Counter

with open(r"file.csv", 'r', encoding='ANSI') as street:
    fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street", "AdmArea", "District", "RouteNumbers",
              "StationName", "Direction", "Pavilion", "OperatingOrgName", "EntryState", "global_id", "geoData"]

    reader = csv.DictReader(street, fields, delimiter=';')
    count_street = [row['Street'] for row in reader]
    print("Больше всего остановок на: {}".format(Counter(count_street).most_common(1)[0][0]))