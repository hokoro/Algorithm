T = int(input())

answers = []


for _ in range(T):
    a,b = map(int,input().split(','))

    answers.append(a+b)



for ans in answers:
    print(ans,end = '\n')