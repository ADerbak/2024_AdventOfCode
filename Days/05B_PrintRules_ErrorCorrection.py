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
corrected_median_value_sum = 0

for rule in rule_list:
    # if primary and secondary page are in our list of tupes,
    # then we can get the median value
    list_of_rules = zip(rule, rule[1:])
    if all((primary_page, secondary_page) in order_list for primary_page, secondary_page in list_of_rules):
        # Get Median
        median_value_sum += int(rule[math.ceil(len(rule)/2)-1])
    
    # Part 2: Handle the out of order pages
    else:
        temp_rule = rule[:]
        i = 0
        while not all((temp_primary_page, temp_secondary_page) in order_list for temp_primary_page, temp_secondary_page in zip(temp_rule, temp_rule[1:])):
            for temp_primary_page, temp_secondary_page in zip(temp_rule, temp_rule[1:]):
                # If we reach end, loop back to 0
                if i + 1 >= len(temp_rule):
                    i = 0
                if (temp_primary_page, temp_secondary_page) not in order_list:
                    # Bubble sort - swap positions
                    temp_rule[i], temp_rule[i + 1] = temp_rule[i + 1], temp_rule[i]
                i += 1
        corrected_median_value_sum += int(temp_rule[math.ceil(len(temp_rule) / 2)-1])

    
print(corrected_median_value_sum)
                
                
            
            