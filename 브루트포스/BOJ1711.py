import sys

input = sys.stdin.readline

n = int(input())

spot = [list(map(int, input().split())) for _ in range(n)]
spot.sort(key=lambda x: [-x[0], -x[1]])
answer = 0
for i in range(0, len(spot) - 2):
    for j in range(i + 1, len(spot) - 1):
        for k in range(j + 1, len(spot)):
            # i 제일 크고 그다음 j 그다음 k
            answer += 1
print(answer)
