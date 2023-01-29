a,b = map(int,input().split())
nums = []
for i in range(1,b+1):
    for j in range(1,i+1):
        nums.append(i)


print(sum(nums[a-1:b]))
