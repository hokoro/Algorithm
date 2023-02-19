# DFS
import sys

sys.setrecursionlimit(10000)
n = int(input())


def isPrime(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def dfs(number):
    if not isPrime(number):
        return
    if len(str(number)) == n:
        print(number)
    for i in range(1, 10, 2):
        dfs(number * 10 + i)
    return


for i in [2, 3, 5, 7]:
    dfs(i)
