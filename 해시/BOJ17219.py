import sys
input = sys.stdin.readline
pw_dict = dict()
n, m = map(int, input().split())
for i in range(n+m):
    if i >= n:
        link = input().strip()
        print(pw_dict[link])
    else:
        link, pw = input().rstrip().split()
        pw_dict[link] = pw_dict.setdefault(link, pw)
