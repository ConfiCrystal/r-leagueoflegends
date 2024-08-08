import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
import csv
from datetime import datetime
              
# Sample dataset
data = {}
filename = "sentimentV2.csv"
with open(filename, 'r') as csvFile:
    csvfile = csv.reader(csvFile)
    data = [{k: v for k, v in row.items()}
        for row in csv.DictReader(csvFile, skipinitialspace=True)]

df = pd.DataFrame(data)

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.25)

# Converting text into vectors
vectorizer = CountVectorizer(stop_words=stopwords.words("english"))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
model = OneVsRestClassifier(SVC()).fit(X_train_vec, y_train)

predictions = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))

# Read CSV file in chunks and process each chunk
chunk_size = 1000
csv_file_path = 'submissionData.csv'
# [0] = id, [1] = datetime, [2] = title, [3] = user, [4] = url, [5] = content
reader = pd.read_csv(csv_file_path, header=None, chunksize=chunk_size)

months = {}
for i, chunk in enumerate(reader):
    print(f'Processing Chunk {i+1}')
    for index, row in chunk.iterrows():
        date = datetime.strptime(row[1][:7], "%Y-%m")
        title = pd.DataFrame([{"text" : str(row[2])}])["text"]
        sent = int(model.predict(vectorizer.transform(title))[0])
        if date in months:
            months[date][sent] += 1
        else:
            months[date] = {-1 : 0, 0 : 0, 1 : 0}
            months[date][sent] += 1

data = []
for date in months:
     data.append({"date" : date, "neg" : months[date][-1], "neu" : months[date][0], "pos" : months[date][1]})

fields = ["date", "neg", "neu", "pos"]
with open("leagueoflegends.csv", 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)