example = input().split('-')
result = 0
print(example)

for i in example[0].split('+'):
    print(i)
    result += int(i)

for i in example[1:]:
    for j in i.split('+'):
        result -= int(j)


print(result)