n, m = map(int, input().split())
listen = []
see = []
answer = []
for _ in range(n):
    listen.append(input())

for _ in range(m):
    see.append(input())

listen = set(listen)

see = set(see)

answer = list(listen & see)

answer.sort()

print(len(answer))
for ans in answer:
    print(ans,end = '\n')