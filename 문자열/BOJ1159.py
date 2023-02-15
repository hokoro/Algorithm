num = int(input())
member_dict = dict()
answer = ''
for _ in range(num):
    name = input()
    if name[0] not in member_dict.keys():
        member_dict[name[0]] = 1
        continue
    else:
        member_dict[name[0]] += 1

members = []
for k,i in member_dict.items():
    if i >= 5:
        members.append([k,i])

members.sort(key=lambda x:[x[0]])

if len(members) == 0:
    answer = 'PREDAJA'
else:
    for member in members:
        answer += member[0]
print(answer)
