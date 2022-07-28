num = int(input())

member = list(map(int,input().split()))

count = 0
member.sort()
group_count = member[0]


print(member)
for i in range(1,len(member)):
    print('group_count: ',group_count)
    print('member: ',member[i])
    print('count: ',count)
    group_count -= 1

    if group_count == 0:
        count += 1
        group_count = member[i+1]



print(count)