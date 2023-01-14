n, m, k = map(int, input().split())
answer = 0
while True:
    if (n - 2) + (m - 1) < k:
        break
    if n < 2 or m < 1:
        break

    else:
        n -= 2
        m -= 1
        answer += 1

print(answer)
