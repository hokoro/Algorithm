import sys

input = sys.stdin.readline

n = int(input())

scores = [int(input()) for _ in range(n)]
answer = 0
target = scores.pop(0)
while True:
    if len(scores) == 0:
        break
    if target > max(scores):
        break

    max_idx = scores.index(max(scores))

    if target <= scores[max_idx]:
        target += 1
        scores[max_idx] -= 1
        answer += 1
print(answer)