num = int(input())

answer = 0
n_sum = 0
for i in range(1,num+1):
    num_char = list(str(i))
    n_sum = i
    for c in num_char:
        n_sum += int(c)
    if n_sum == num:
        answer = i
        break
    else:
        continue
print(answer)