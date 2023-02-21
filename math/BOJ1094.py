num = int(input())

answer = 0
start = 64
while num != 0:
    if start > num:
        start = start // 2

    else:
        num -= start
        answer += 1
        start = start //2

print(answer)