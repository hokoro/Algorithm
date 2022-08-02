h, m = map(int, input().split())

h_count = 0
CookTime = int(input())

m = m + CookTime

if m > 59 and m % 60 == 0:
    h_count = m // 60
    m = 0

if m > 59:
    h_count = m // 60
    m = m - (60*h_count)

print(f'{(h+h_count)%24} {m}')