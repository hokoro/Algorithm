answer = ''
array = []
max_len =0
for _ in range(5):
    words = list(input())
    array.append(words)
    if len(words) > max_len:
        max_len = len(words)
for i in range(5):
    if max_len > len(array[i]):
        for _ in range(max_len - len(array[i])):
            array[i].append('')

for i in range(max_len):
    for j in range(5):
        print(array[j][i],end='')




