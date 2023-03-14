import sys

input = sys.stdin.readline

n, k = map(int, input().split())

numbers = []
temp = []

for i in range(n):
    numbers.append(1)
    temp.append(1)
    if i < 2:
        pass
    else:
        for j in range(1, len(numbers) - 1):
            temp[j] = numbers[j - 1] + numbers[j]
    for j in range(len(numbers)):
        numbers[j] = temp[j]


print(numbers[k-1])
