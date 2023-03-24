import sys

input = sys.stdin.readline
answer = []

n, k = map(int, input().split())

visited = [False] * (n + 1)

for i in range(2, n + 1):
    if visited[i]:
        continue
    else:
        num = 1
        for j in range(1, n + 1):
            num = i * j
            if num > n:
                break
            else:
                if not visited[num]:
                    visited[num] = True
                    answer.append(num)

print(answer[k-1])
