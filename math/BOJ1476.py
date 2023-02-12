e, s, m = map(int, input().split())

answer = 1

year = [1, 1, 1]

while year != [e, s, m]:
    answer += 1
    year[0] = 15 if (year[0] + 1) % 15 == 0 else (year[0] + 1) % 15
    year[1] = 28 if (year[1] + 1) % 28 == 0 else (year[1] + 1) % 28
    year[2] = 19 if (year[2] + 1) % 19 == 0 else (year[2] + 1) % 19


print(answer)
