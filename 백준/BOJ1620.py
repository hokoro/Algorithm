n, m = map(int, input().split())
pocketmon_list = []
for i in range(n+m):
    s = input()
    if i < n:
        pocketmon_list.append(s)
    else:
        if s.isdecimal():
            print(pocketmon_list[int(s)-1])
        else:
            print(pocketmon_list.index(s)+1)
