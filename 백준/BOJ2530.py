h,m,s = map(int,input().split())
time = int(input())

minites = time // 60
second = time % 60


if s + second >= 60:
    m = m + (s+second) // 60
    s = (s+second) % 60
else:
    s = s + second

if m + minites >= 60:
    h = h + (m+minites) // 60
    m = (m + minites) % 60

else:
    m = m + minites
if h > 23:
    h = h % 24

print(f'{h} {m} {s}')