import sys

input = sys.stdin.readline

n, k = map(int, input().split())

countrys = []
for _ in range(n):
    country = list(map(int, input().split()))
    countrys.append(country)

countrys.sort(key=lambda x: [-x[1], -x[2], -x[3]])

idx = [countrys[i][0] for i in range(n)].index(k)

for i in range(n):
    if countrys[idx][1:] == countrys[i][1:]:
        print(i+1)
        break