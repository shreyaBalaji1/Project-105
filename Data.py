import csv
import math

with open("data.csv", newline = "") as f :
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

#finding the mean
def mean(data) :
    sum = 0
    n = len(data)

    for i in data :
        sum = sum + int(i)

    mean = sum/n
    return mean

#subtracting from the mean & squaring it
squaredList = []
for i in data :
    a = int(i) - mean(data)
    a = a**2
    squaredList.append(a)

#summing the squared List
sum = 0
for j in squaredList :
    sum = sum + j

#dividing by total values (n-1)
result = sum/(len(data) -1)

#square rooting
stdev = math.sqrt(result)

print(stdev)