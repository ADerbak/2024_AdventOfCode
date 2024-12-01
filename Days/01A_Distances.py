import requests

data = []
data_1 = []
data_2 = []
filename = './Days/01A_data.txt'
with open(filename, 'r') as f:
    lines= f.readlines()

# print(lines)
for line in lines:
    data.append(line.strip('\n').split('   '))

for record in data:
    data_1.append(record[0])
    data_2.append(record[1])
    
data_1 = sorted(data_1)
data_2 = sorted(data_2)

sum = 0
for i in range(0,len(data_1)):
    amt =  abs(int(data_2[i]) - int(data_1[i]))
    sum += amt
    
print(sum) 