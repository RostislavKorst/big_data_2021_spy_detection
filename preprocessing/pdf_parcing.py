import pandas as pd
import string
import numpy as np
from tqdm import tqdm

f = open('skyteam.txt')
df = pd.DataFrame(columns=['ind','Validity', 'Days', 'Dep Time','Arr Time', 'Flight', 'Aircraft','Travel Time','FROM', 'TO'])

num = 0
for j,line in enumerate(tqdm(f)):
    arr = line.split(" ")
    if arr[0] == 'Operated':
        continue
    if arr[0] == 'FROM:':
        arr[-1] = arr[-1].replace("\n", "")
        FROM = " ".join(arr[1:])
        continue
    if arr[0] == 'TO:':
        arr[-1] = arr[-1].replace("\n", "")
        TO = " ".join(arr[1:])
        continue
    if arr[0] == 'Validity':
        continue
    if arr[0] == 'Time\n':
        continue
    if arr[0] == 'Arr\n':
        continue
    if arr[0] == 'Flight':
        continue
    if arr[0] == 'Consult':
        continue
    else:
        val = (arr[0] + ' ' + arr[1] + ' ' + arr[2] + ' ' + arr[3] + ' ' + arr[4])
        for j, i in enumerate(arr[5:]):
            if (str.find(i, ':') != -1):
                break
        index = 5 + j
        days = " ".join(arr[5:index])
        dep_time = arr[index]
        arr_time = arr[index + 1]
        flight = arr[index + 2]
        aircraft = arr[index + 3]
        travel_time = arr[index + 4]
        travel_time = travel_time.replace("\n", "")
        df2 = pd.DataFrame([[num, val, days, dep_time, arr_time, flight, aircraft, travel_time, FROM, TO]],
                           columns=['ind', 'Validity', 'Days', 'Dep Time', 'Arr Time', 'Flight', 'Aircraft',
                                    'Travel Time', 'FROM', 'TO'])
        df = df.append(df2)
        num += 1

df = df.set_index('ind')
df.to_csv("skyteam.csv", sep='\t')