import sys


def sosu(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = 1
token = []
for num in nums:
    if sosu(num) and num not in token:
        answer *= num
        token.append(num)

print(answer if answer > 1 else -1)
