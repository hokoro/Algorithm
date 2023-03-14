n = int(input())

nums = [list(map(int,input().split())) for _ in range(n)]

nums.sort(key=lambda x:[x[0],x[1]])
answer = 0

for num in nums:
    if num[0] >= answer:
        answer = num[0] + num[1]
    else:
        answer += num[1]

print(answer)