import csv
import json


# CSV to JSON method by https://pythonexamples.org/python-csv-to-json/
# --------------------------------------------------------------------

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'data.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)


# CSV to JSON
# --------------------------------------------

with open("C:\\Users\\anurd\\Desktop\\wos-engineering.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"Journal Name": row[0],
                     "Publisher": row[1],
                     "ISSN / eISSN": row[2],
                     "Web of Science Core Collection": row[3],
                     "Additional Web of Science Indexes": row[4],
                     "Journal Website": row[5],
                     "Publication Frequency": row[6],
                     "Aims and Scope": row[7],
                     "Indexing and Abstracting": row[8]})

with open("C:\\Users\\anurd\\Desktop\\wos-engineering.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        row[8] = row[8].strip()
        line = row[8].replace(".\n\n", " ")
        line = line.replace("\n\n", ", ")
        line = line.replace("\n", ", ")
        line = line.replace("; ", ", ")
        data.append(line)

with open("wos-engineering.json", 'w', encoding='utf-8') as f:
    jsonFile = json.dumps(data, indent=4)
    f.write(jsonFile)


# Excel to CSV
# -------------------

import pandas as pd


def excel_to_csv(excelFilePath, csvFilePath):
    read_file = pd.read_excel(excelFilePath)
    read_file.to_csv(csvFilePath, index=None, header=True)


excelFilePath = r'C:\\Users\\anurd\\Desktop\\wos-engineering.xlsx'
csvFilePath = r'C:\Users\anurd\Desktop\wos-engineering.csv'
excel_to_csv(excelFilePath, csvFilePath)
