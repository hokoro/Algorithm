n = int(input())

for i in range(n):
    sum_ = 0
    a = int(input())
    for j in range(1, a+1):
        sum_ += (a//j)*j
    print(sum_)