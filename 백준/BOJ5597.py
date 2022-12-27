answer_list = [0] * 30

for _ in range(28):
    n = int(input())
    answer_list[n - 1] = 1
for _ in range(2):
    position = answer_list.index(0)
    print(position+1)
    answer_list[position] = 1
