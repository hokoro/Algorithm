num = int(input())
rooms = [tuple(map(int, input().split())) for _ in range(num)]
answer = 0

rooms.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간을 기준으로 정렬

end = 0  # 미팅이 끝나는 시간을 담는 변수

for room in rooms:  # 정렬된 회의실 시간을 반복문을 돌면서
    if room[0] >= end:  # 마지막으로 회의가 끝나는 시간이 시작 시간보다 작거나 같다면 그 다음 회의
        end = room[1]   # 마지막으로 회의가 끝나느 시간을 초기화 하고
        answer += 1  # 정답 을 +=1

print(answer)
