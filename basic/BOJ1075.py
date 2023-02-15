a = int(input())
b = int(input())
answer = str()
a = int(str(a)[:-2] + '00')

while True:
    if a % b == 0:
        break
    a += 1

answer = str(a)[-2:]

print(answer)
