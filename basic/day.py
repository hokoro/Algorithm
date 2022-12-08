a, b, c = map(int, input().split())
d = 1
while True:
    if d % a == 0 and d % b == 0 and d % c == 0:
        print(d)
        break
    d += 1
