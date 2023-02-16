num = int(input())

answer = 0
fact_num = 1
for i in range(2, num + 1):
    fact_num *= i

while True:
    if fact_num % 2 != 0 or fact_num % 5 != 0:
        break
    if fact_num % 2 == 0 and fact_num % 5 == 0:
        fact_num = fact_num // 10
        answer += 1
print(answer)
