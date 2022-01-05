N, M, K = map(int, input().split())

number_list = list(map(int, input().split()))

number_list.sort(reverse=True)
first = number_list[0]
second = number_list[1]
number_sum = 0
count = K
for _ in range(M):
    if count == 0:
        number_sum = number_sum + second
        count = K
        continue
    number_sum = number_sum + first
    count = count -1


print(number_sum)