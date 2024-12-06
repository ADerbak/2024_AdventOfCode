import math 
filename = './Days/05A_data.txt'

order_list = []
rule_list = []

with open(filename, 'r') as f:
    for line in f:
        if "|" in line:
            key, value = str(line).strip().split("|")
            order_list.append((key, value))
        if "," in line:
            rule_list.append(str(line).strip().split(','))
            

median_value_sum = 0

for rule in rule_list:
    # if primary and secondary page are in our list of tupes,
    # then we can get the median value
    list_of_rules = zip(rule, rule[1:])
    print(list_of_rules)
    if all((primary_page, secondary_page) in order_list for primary_page, secondary_page in list_of_rules):
        # Get Median
        median_value_sum += int(rule[math.ceil(len(rule)/2)-1])
    
        

    
print(median_value_sum)
                
                
            
            