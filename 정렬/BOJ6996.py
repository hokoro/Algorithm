import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = map(str,input().split())
    str_a = list(a)
    str_b = list(b)
    str_a.sort()
    str_b.sort()
    if str_a == str_b:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')