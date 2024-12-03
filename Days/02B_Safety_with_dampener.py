data = []
safe_reports = 0
filename = './Days/02A_data.txt'
with open(filename, 'r') as f:
    lines= f.readlines()

# print(lines)
for line in lines:
    data.append(line.strip('\n').split(' '))

for i in range(0,len(data)):
    process_list = data[i]
    for k in range(0, len(process_list)):
        # Create a copy of the list without the kth element
        new_list = process_list[:k] + process_list[k+1:]
        prev_safe_reports = safe_reports
        ascending = False
        prev_value = 0
        for j in range(0, len(new_list)):
            value = int(new_list[j])
            if j == 0:
                prev_value = value
                continue
            if j == 1 and value>prev_value:
                ascending = True
            if value > prev_value and ascending != True:
                break
            if value < prev_value and ascending != False:
                break
            if abs(value-prev_value)>3 or value == prev_value:
                break
            if j == len(new_list)-1:
                safe_reports += 1
                break
            prev_value = value
        
        if prev_safe_reports + 1 == safe_reports:
            break
        
        
print(safe_reports)