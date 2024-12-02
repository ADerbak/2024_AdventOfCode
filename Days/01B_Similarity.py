import requests

data = []
data_1 = {}
data_2 = []
filename = './Days/01A_data.txt'
with open(filename, 'r') as f:
    lines= f.readlines()

for line in lines:
    data.append(line.strip('\n').split('   '))

for record in data:
    data_1[record[0]] = 0
    data_2.append(record[1])
    

for i in range(0,len(data_2)):
    if data_2[i] in data_1:
        data_1[data_2[i]] += 1

sum = 0
for k,v in data_1.items():
    sum += int(k) * v
print(sum) 