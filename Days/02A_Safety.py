data = []
safe_reports = 0
filename = './Days/02A_data.txt'
with open(filename, 'r') as f:
    lines= f.readlines()

# print(lines)
for line in lines:
    data.append(line.strip('\n').split(' '))

for i in range(0,len(data)):
    prev_value = 0
    ascending = False
    for j in range(0, len(data[i])):
        value = int(data[i][j])
        if j == 0:
            prev_value = value
            continue
        if j == 1 and value>prev_value:
            ascending = True
        if (value > prev_value and ascending != True):
            break
        if (value < prev_value and ascending != False):
            break
        if abs(value-prev_value)>3 or value == prev_value:
            break
        if j == len(data[i])-1:
            safe_reports += 1
            break
        prev_value = value
        
print(safe_reports)