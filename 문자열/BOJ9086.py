n = int(input())
answers = []

for _ in range(n):
    lines = input()
    answers.append(lines[0] + lines[-1])


for answer in answers:
    print(answer , end='\n')
