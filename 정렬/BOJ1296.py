name = input()
answer = ''
MAX = 0
t = int(input())
name_counts = [0, 0, 0, 0]
for s in name:
    if s == 'L':
        name_counts[0] += 1
    elif s == 'O':
        name_counts[1] += 1
    elif s == 'V':
        name_counts[2] += 1
    else:
        name_counts[3] += 1

for _ in range(t):
    name_ = list(input())
    counts = [0, 0, 0, 0]
    for s in name_:
        if s == 'L':
            counts[0] += 1
        elif s == 'O':
            counts[1] += 1
        elif s == 'V':
            counts[2] += 1
        else:
            counts[3] += 1
    l, o, v, e = name_counts[0] + counts[0], name_counts[1] + counts[1], name_counts[2] + counts[2], name_counts[3] + counts[3]
    cacul = ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
    if cacul >= MAX:
        MAX = cacul
        answer = name_


print(''.join(answer))
