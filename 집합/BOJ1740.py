import sys

sys.setrecursionlimit(5 * 10 ** 8)
input = sys.stdin.readline

num = int(input())


def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return rev_base[::-1]


number = 1
while num != 0:
    result = solution(number)

    flag = True
    for i in range(len(result)):
        if int(result[i]) > 1:
            flag = False
            break
    if flag:
        num -= 1

    number += 1

print(number - 1)
