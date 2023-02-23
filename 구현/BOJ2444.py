import sys
input = sys.stdin.readline

n = int(input())
stars = ['*' * (2*i-1) for i in range(1,n+1)]
stars += (reversed(stars[:n-1]))
nums = [' ' * (n-1-i) for i in range(n)]
nums += (reversed(nums[:n-1]))

for n,s in zip(nums,stars):
    print(n+s+n)