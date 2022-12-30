n,m = map(int,input().split())

answer = 0
S = []

for i in range(n):
    s = input()
    S.append(s)

for i in range(m):
    s = input()
    if s in S:
        answer+=1


print(answer)