import csv
import json

# " yerine ' ile dosyaya yazıyor
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

# \" ile " olduğu gibi kalıyor. 
# Elasticsearch JSON formatında ' hata veriyor.
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
            number = number + 1
        tx.close()
