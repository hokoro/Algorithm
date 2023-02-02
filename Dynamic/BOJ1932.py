
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
dp = [nums[0]]

arr = [[0 for j in range(len(nums[i]))] for i in range(1,len(nums))]
dp = dp + arr
print(nums)
print(dp)




'''
dp[0+1][0] < dp[0][0+0] + nums[0+1][0]
dp[0+1][1]< dp[0][0+1] + nums[0+1][1]
'''

# nums = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# dp = [[7], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
#
# print(dp[1][0] < dp[0][0] + nums[1][0])
# #print(dp[1][1] < dp[0][0] + nums[1][1])
# print(dp[1][1])
# print(dp[0][1])
# print(nums[1][1])