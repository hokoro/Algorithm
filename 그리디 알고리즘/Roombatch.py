N = int(input())
meeting_list = [tuple(map(int, input().split())) for _ in range(N)]
meeting_count = 0

meeting_list.sort(key=lambda x: (x[1], x[0]))

endmeeting = 0
for meet in meeting_list:
    if meet[0] >= endmeeting:
        endmeeting = meet[1]
        meeting_count += 1

print(meeting_count)
