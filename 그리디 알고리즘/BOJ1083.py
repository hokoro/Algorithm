num_len = int(input())
nums = list(map(int, input().split()))
count = int(input())

for i in range(num_len - 1):
    if count == 0:
        break
    mx,idx = nums[i],i
    for j in range(i+1,min(num_len,i+1+count)):
        if mx < nums[j]:
            mx = nums[j]
            idx = j
    count -= idx - i

    for j in range(idx,i,-1):
        nums[j] = nums[j-1]
    nums[i] = mx
print(*nums)
