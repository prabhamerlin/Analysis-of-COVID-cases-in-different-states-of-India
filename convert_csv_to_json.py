import json  # This is for working on JSON data
import csv   # This is for working on .csv FILE




with open ("Population.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"Rank" : row[0],
                     "State/UT" : row[1],
                     "Population" : row[2]
                     # "Active cases" : row[3],
                     # "Cured/Discharged" : row[4],
                     # "Death" : row[5]
                     })
with open("Population.json", "w") as f:
    json.dump(data,f,indent=4)