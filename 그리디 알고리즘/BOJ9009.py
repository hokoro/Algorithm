import sys

input = sys.stdin.readline
n = int(input())

fibonachi = [0, 1]

for i in range(2, 46):
    fibonachi.append(fibonachi[i - 1] + fibonachi[i - 2])

for i in range(n):
    num = int(input())
    result = []

    for j in range(len(fibonachi) - 1, 0, -1):
        if fibonachi[j] > num:
            continue
        num -= fibonachi[j]
        result.append(fibonachi[j])
    result.sort()

    for k in result:
        print(k, end=' ')
    print()
