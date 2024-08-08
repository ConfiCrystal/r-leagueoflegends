import pandas as pd
from datetime import datetime
import csv

# Read CSV file in chunks and process each chunk
chunk_size = 1000
csv_file_path = 'submissionData.csv'
# [0] = id, [1] = datetime, [2] = title, [3] = user, [4] = url, [5] = content
reader = pd.read_csv(csv_file_path, header=None, chunksize=chunk_size)

def createDataset(startIndex):
    # Init
    count = 0
    data = []
    fields = ["text", "label"]
    filename = "sentiment.csv"
    out = False

    pos = 0
    neg = 0
    neu = 0
    target = 1000

    for i, chunk in enumerate(reader):
        if out: break
        print(f'Processing Chunk {i+1}')
        for index, row in chunk.iterrows():
            if count >= startIndex:
                title = row[2]

                print("Positive: " + str(pos) + "/" + str(target) + ", Neutral: " + str(neu) + "/" + str(target) + ", Negative: " + str(neg) + "/" + str(target))
                print("Post #" + str(count + 1) + " title:")
                print(title)
                print("Input sentiment (n negative, 0 neutral, p positive)")
                print("'i' to skip and 'q' to finish")

                con = False
                while (True):
                    sentiment = input()
                    print("")
                    if sentiment == "i":
                        con = True
                        break
                    elif sentiment == "q":
                        out = True
                        break
                    elif sentiment == "n":
                        if neg > target: con = True
                        else: neg += 1
                        sentiment = -1
                        break
                    elif sentiment == "0":
                        if neu > target: con = True
                        else: neu += 1
                        sentiment = 0
                        break
                    elif sentiment == "p":
                        if pos > target: con = True
                        else: pos += 1
                        sentiment = 1
                        break
                if out: break
                if con: continue
                count += 1


                data.append({"text" : title, "label" : sentiment})

    with open(filename, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

createDataset(0)