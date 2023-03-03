import sys

input = sys.stdin.readline
count = 0
num = input().rstrip()

while len(num) != 1:
    sum_ = 0
    for n in num:
        sum_ += int(n)
    count += 1
    num = str(sum_)
print(count)
print('YES' if int(num) % 3 == 0 else 'NO')



