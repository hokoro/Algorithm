
answers = []
T = int(input())

for _ in range(T):
    num = int(input())
    padoban = [1, 1, 1]
    for i in range(3,num):
        padoban.append(padoban[i-2] + padoban[i-3])

    answers.append(padoban[-1])



for answer in answers:
    print(answer , end = '\n')




