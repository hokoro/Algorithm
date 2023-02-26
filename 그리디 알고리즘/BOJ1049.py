n, m = map(int, input().split())
s_min = 1000
l_min = 1000
for _ in range(m):
    s, l = map(int, input().split())
    if s_min > s:
        s_min = s

    if l_min > l:
        l_min = l

set_ = 0
set_piece = s_min * (n // 6) + l_min * (n % 6)
piece_ = l_min * n
if n % 6 == 0:
    set_ = s_min * (n // 6)
else:
    set_ = s_min * ((n // 6) + 1)

print(min(set_,set_piece,piece_))


