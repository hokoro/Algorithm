salt = int(input())
answer = 0

while True:
    if salt < 0:
        answer = -1
        break
    if salt % 5 == 0:
        answer = answer + (salt // 5)
        break
    salt = salt - 3
    answer = answer + 1


print(answer)
