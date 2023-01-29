import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
pocketmon_dict = defaultdict()
reverse_pocketmon_dict = defaultdict()
answers = []
for i in range(0, n + m):
    if i < n:
        monster = sys.stdin.readline().replace('\n', '')
        pocketmon_dict.setdefault(str(i + 1), monster)
        reverse_pocketmon_dict.setdefault(monster, str(i + 1))
        continue

    else:
        question = sys.stdin.readline().replace('\n', '')
        if question.isdigit():
            answers.append(pocketmon_dict[question])
        else:
            answers.append(reverse_pocketmon_dict[question])

for ans in answers:
    print(ans, end='\n')
