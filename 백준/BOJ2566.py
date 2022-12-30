board = [list(map(int,input().split())) for _ in range(9)]
answer = 0
answer_row = 0
answer_col = 0
row_index = 0
for row in board:
    if answer < max(row):
        answer = max(row)
        answer_col = row.index(max(row))
        answer_row = row_index
    row_index += 1

print(answer)
print(f"{answer_row+1} {answer_col+1}")