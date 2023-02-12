n = int(input())
nums = [i for i in range(10)]
alpha_dict = dict()

answer = ''
alpha_list = ['' for _ in range(8)]
max_size = 0
for _ in range(n):
    alpha = input()
    alpha = list(alpha)
    if max_size < len(alpha):
        max_size = len(alpha)
    for i in range(-1, -(len(alpha) + 1), -1):
        alpha_list[i] = alpha_list[i] + alpha[i]

alpha_list = alpha_list[len(alpha_list) - max_size:]
evals = ''.join(alpha_list)

for al in evals:
    if al in alpha_dict.keys():
        continue
    else:
        alpha_dict[al] = nums.pop()


up = 0


for i in range(len(alpha_list) - 1, -1, -1):
    num_sum = 0
    for token in alpha_list[i]:
        num_sum += alpha_dict[token]

    num_sum += up

    if num_sum >= 10:
        up = int(str(num_sum)[0])
        answer = str(num_sum)[-1] + answer
    else:
        up = 0
        answer = str(num_sum) + answer

if up >= 1:
    answer = str(up) + answer

print(int(answer))
