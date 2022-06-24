num = int(input())
answer = 0

for i in range(1, num + 1):
    answer += (num // i)*i

print(answer)
