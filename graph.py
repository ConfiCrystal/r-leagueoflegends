import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.dates import date2num

data = {}
filename = "leagueoflegendsV1.csv"
with open(filename, 'r') as csvFile:
    csvfile = csv.reader(csvFile)
    data = [{k: v for k, v in row.items()}
        for row in csv.DictReader(csvFile, skipinitialspace=True)]
    
data = sorted(data, key = lambda d:d["date"])

dates = []
positives = []
neutrals = []
negatives = []

for i, tuple in enumerate(data):
    dates.append(datetime.strptime(tuple["date"], "%Y-%m-%d %H:%M:%S"))
    sum = int(tuple["pos"]) + int(tuple["neu"]) + int(tuple["neg"])
    positives.append(int(tuple["pos"]) / sum * 100)
    neutrals.append(int(tuple["neu"]) / sum * 100)
    negatives.append(int(tuple["neg"]) / sum * 100)
dates = date2num(dates)

ax = plt.subplot(111)
ax.plot(dates, positives, color='g')
ax.plot(dates, neutrals, color='y')
ax.plot(dates, negatives, color='r')
ax.xaxis_date()
ax.set_ylim([0, 100])
ax.set_ylabel("% of posts")
ax.set_xlabel("date")
ax.legend(["positive posts", "neutral posts", "negative posts"])
ax.set_title("r/leagueoflegends")

plt.show()