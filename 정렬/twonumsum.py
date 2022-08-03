t = int(input())

nums = list(map(int, input().split()))

x = int(input())

nums.sort()

count = 0
left,right = 0 , t-1


while left < right:
    numsum = nums[left] + nums[right]
    if nums[left] + nums[right] == x:
        count+= 1

    if numsum < x:
        left += 1
        continue
    right -= 1

print(count)

