def solution(id_list, report, k):
    answer = []
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

k = 2
answer = []
#신고 당한 사람
Perpetrator = {}

#신고 한 사람
Victim = {}

report_dict ={}

for id in id_list:
    Perpetrator[id] = 0
    Victim[id] = {}

for rep in report:
    rep = rep.split(' ')
    Perpetrator[rep[1]] += 1

    if rep[1] in Victim[rep[0]]:
        continue
    else:
        Victim[rep[0]][rep[1]] = 1

value = list(Perpetrator.values())
key = list(Perpetrator.keys())


# for i in range(len(value)):
#     if value[i] >= k:
#         if key[i] in

print(Perpetrator)
print(Victim)

print(report_dict)