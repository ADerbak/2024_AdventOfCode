filename = './Days/04A_data.txt'

xmas_matrix = []

with open(filename, 'r') as f:
    for line in f:
        row = [x for x in str(line).strip('\n')]
        xmas_matrix.append(row)
        
# specify directions to check
rows, cols = len(xmas_matrix), len(xmas_matrix[0])

xmas_count = 0
wordpart = "MS"

def is_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols

for row in range(rows):
    for col in range(cols):
        if xmas_matrix[row][col] == 'A':
            for dr, dc in [(1, 1), (1, -1)]:
                temp_row = row+dr
                temp_col = col+dc
                
                opposite_temp_row = row + dr * -1
                opposite_temp_col = col + dc * -1
                
                adj_temp_row = row + dr
                adj_temp_col = col + dc * -1
                
                opp_adj_temp_row = row + dr * -1
                opp_adj_temp_col = col + dc
                
                if is_valid(temp_row, temp_col) and is_valid(opposite_temp_row, opposite_temp_col) \
                    and is_valid(adj_temp_row, adj_temp_col) and is_valid(opp_adj_temp_row, opp_adj_temp_col):
                    temp_char = xmas_matrix[temp_row][temp_col] 
                    opposite_temp_char = xmas_matrix[opposite_temp_row][opposite_temp_col]
                    adj_temp_char = xmas_matrix[adj_temp_row][adj_temp_col] 
                    opp_adj_temp_char = xmas_matrix[opp_adj_temp_row][opp_adj_temp_col]
                    
                    if temp_char in wordpart \
                        and opposite_temp_char in wordpart \
                        and adj_temp_char in wordpart \
                        and opp_adj_temp_char in wordpart \
                        and temp_char != opposite_temp_char \
                        and adj_temp_char != opp_adj_temp_char:
                        
                        xmas_count += 1 
                        break

print(xmas_count)
                