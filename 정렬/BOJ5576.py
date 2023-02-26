ws = []
ks = []

for _ in range(10):
    num = int(input())
    ks.append(num)

for _ in range(10):
    num = int(input())
    ws.append(num)

ks.sort(reverse=True)
ws.sort(reverse=True)

print(sum(ks[:3]) , sum(ws[:3]))