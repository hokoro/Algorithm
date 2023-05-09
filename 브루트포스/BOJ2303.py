n = int(input())
ans = []
MAX = 0
for _ in range(n):
    nums = list(map(int,input().split()))
    for i in range(len(nums)-2):
        for j in range(1,len(nums)-1):
            for k in range(2,len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if int(str(num)[-1]) > MAX:
                    MAX = int(str(num)[-1])

    ans.append(MAX)

print(ans.index(MAX)+1)
