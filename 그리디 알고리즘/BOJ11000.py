n = int(input())
rooms = [list(map(int, input().split())) for _ in range(n)]

end = [0]

rooms.sort(key=lambda x: (x[0], x[1])) # 회의실 배정 문제와 다르게 출발을 기준으로 정렬 한다.


for room in rooms:
    if room[0] >= min(end):
        end.remove(min(end))
        end.append(room[1])

    else:
        end.append(room[1])

print(len(end))