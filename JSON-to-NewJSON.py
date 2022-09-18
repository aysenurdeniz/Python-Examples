import csv
import json

with open("C:\\Users\\anurd\\Downloads\\googleplaystore_user_reviews.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    number = 1
    for row in reader:
        data.append({"create": {"_index": "papers", "_id": number}})
        data.append({"App": row[0],
                     "Translated_Review": row[1],
                     "Sentiment": row[2],
                     "Sentiment_Polarity": row[3],
                     "Sentiment_Subjectivity": row[4]})
        number = number + 1

with open("C:\\Users\\anurd\\Downloads\\googleplaystore_user_reviews.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    number = 1
    st = '{\"create\": {\"_index\": \"papers\", \"_id\": \"'
    strdata = ['{\"App\":\"', '\", \"Translated_Review\":\"', '\", \"Sentiment\":\"', '\", \"Sentiment_Polarity\":\"', '\", \"Sentiment_Subjectivity\":\"']
    with open("new.txt", "w") as tx:
        for row in reader:
            tx.write(st + str(number) + "\"}\n")
            tx.write(strdata[0] + str(row[0]) + strdata[1] + str(row[1]) + strdata[2] + str(row[2]) + strdata[3] + str(row[3]) + strdata[4] + str(row[4])+"\"}\n")
            # ths.write("{'create': {'_index': 'papers', '_id': number}\n}")
            # ths.write("{'App': {},'Translated_Review': {}, 'Sentiment': {}, 'Sentiment_Polarity': {}, "
            #           "'Sentiment_Subjectivity': {}}\n "
            #           .format(row[0], row[1], row[2], row[3], row[4]))
            number = number + 1
        tx.close()

# with open("C:\\Users\\anurd\\PycharmProjects\\imageProcessing\\papers.json") as fil:
#     text = fil.read()
#     text.replace("}, {", "}/n{")
#     fil.write(text)


# next(veri)
#     data = []
#     for row in veri:
#         line = row.replace("}, {", "}\n{")
#         data.append(line)

with open("papers.json", 'w', encoding='utf-8') as f:
    jsonString = json.dumps(data, indent=0)
    f.write(jsonString)
