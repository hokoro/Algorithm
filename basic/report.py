# def solution(id_list, report, k):
#     answer = []
#     report_count = [0] * len(id_list)
#     report_id_dict = {id: list() for id in id_list}
#     stop_id_dict = {id: list() for id in id_list}
#     for re in report:
#         r = re.split(" ")
#         report_count[id_list.index(r[1])] += 1
#         report_id_dict[r[0]].append(r[1])
#     for i in range(len(report_count)):
#         for info in report_id_dict:
#             if report_count[id_list.index(info)] == k and info in report_id_dict[id_list[i]] :
#                 stop_id_dict[id_list[i]].append(info)
#             elif report_count[id_list.index(info)] > k and info in report_id_dict[id_list[i]]:
#                 stop_id_dict[id_list[i]].append(0)
#
#     answer = [len(stop_id_dict[id])for id in id_list]
#     return answer
from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)



    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a, b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]

k = 2
print(solution(id_list, report, k))
