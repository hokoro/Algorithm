import sys

input = sys.stdin.readline

answer = 0
n, l, k = map(int, input().split())
count = 0
scores = []
for _ in range(n):
    sub1, sub2 = map(int, input().split())
    scores.append([sub1, sub2])

scores.sort(key=lambda x: [x[1], x[0]])

for score in scores:
    if count == k:
        break
    else:
        if score[1] <= l:
            answer += 140
            count += 1
            continue
        if score[0] <= l:
            answer += 100
            count += 1
            continue
print(answer)
