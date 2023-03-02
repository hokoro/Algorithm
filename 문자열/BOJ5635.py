import sys

input = sys.stdin.readline

n = int(input())
members = []
for _ in range(n):
    member = list(map(str, input().split()))
    member[0] = member[0].rstrip()
    member[1] = int(member[1].rstrip())
    member[2] = int(member[2].rstrip())
    member[3] = int(member[3].rstrip())
    members.append(member)
members.sort(key=lambda x: [-int(x[3]), -int(x[2]), -int(x[1])])

print(members[0][0])
print(members[-1][0])
