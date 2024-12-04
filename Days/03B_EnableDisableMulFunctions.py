import re

filename = './Days/03A_data.txt'

with open(filename, 'r') as f:
    data = f.readlines()

muls = []
for line in data:
    muls.extend(re.findall(r'do(?:n\'t)?\(\)|mul\(\d{1,3}\,\d{1,3}\)', line))

total = 0
do = True
for mul in muls:
    if mul == 'do()':
        do = True
    if mul == "don't()":
        do = False
    if do and "mul" in mul:
        muls_sum = int(re.findall(r'\d{1,3}', mul)[0]) * int(re.findall(r'\d{1,3}', mul)[1])
        total += muls_sum
    
print(total)