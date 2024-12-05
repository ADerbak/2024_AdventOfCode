filename = './Days/04A_data.txt'

xmas_matrix = []

with open(filename, 'r') as f:
    for line in f:
        row = [x for x in str(line).strip('\n')]
        xmas_matrix.append(row)
        
# specify directions to check
rows, cols = len(xmas_matrix), len(xmas_matrix[0])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

xmas_count = 0
word = "XMAS"



for row in range(rows):
    for col in range(cols):
        for direction in directions:
            temp_row = row
            temp_col = col
            process = True
            dr, dc = direction
            i = 0
            for _ in range(len(word)):
                if 0 > temp_row or temp_row > rows-1:
                    process = False
                    break
                if  0 > temp_col or temp_col > cols-1:
                    process = False
                    break
                if xmas_matrix[temp_row][temp_col] != word[i]:
                    process = False
                    break
                temp_row += dr
                temp_col += dc
                i += 1
            if process:
                xmas_count += 1
                
print(xmas_count)