import math

while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break

    nums = []
    for i in range(2,int(math.sqrt(b)+1)):
        if b % i == 0:
            nums.append(i)
            nums.append(b // i)
        if a in nums:
            answer = 'factor'
            break


