import sys

N = int(sys.stdin.readline())
answer = 0
while N != 1:
    for i in range(3, 1, -1):
        target = (N // i) * i
        answer += (N - target)
        N = target
        answer += 1
        N //= i

    answer += (N - 1)

print(answer)
