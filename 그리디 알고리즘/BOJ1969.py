import sys
input = sys.stdin.readline
answer = 0
answer_str = ''
n,m = map(int,input().split())
dnas = []
answers = []
for _ in range(n):
    dna = input().rstrip()
    dnas.append(dna)

for i in range(m):
    char_dict = dict()
    for j in range(n):
        char_dict[dnas[j][i]] = char_dict.setdefault(dnas[j][i],0) + 1
    char_list = list(char_dict.items())
    char_list.sort(key=lambda x : (-x[1] , x[0]))
    answer += (n - char_list[0][1])
    answer_str += char_list[0][0]


print(answer_str)
print(answer)