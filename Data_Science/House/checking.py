import csv

with open('777.csv') as file:

    reader = csv.reader(file, delimiter=',')

    count = 0

    for row in reader:
        print(row)
        count += 1

# print(count)

import pandas as pd
from pandas import DataFrame

file = pd.read_csv('777.csv')
df = DataFrame(file)
print(df)