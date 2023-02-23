import math

m = int(input())
n = int(input())
answers = []
for i in range(m,n+1):
    number = math.sqrt(i)
    if int(number) == number:
        answers.append(i)

if len(answers) > 0:
    print(sum(answers))
    print(min(answers))
else:
    print(-1)