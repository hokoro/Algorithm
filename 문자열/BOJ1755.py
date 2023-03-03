m, n = map(int, input().split())

number = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero',
}

nums = []
for i in range(m, n + 1):
    num = str(i)
    token = ''
    for n in num:
        token = token + number[n] + ' '

    nums.append([i, token[:-1]])

nums.sort(key=lambda x: [x[1], x[0]])

for i in range(len(nums)):
    print(nums[i][0], end=' ')
    if (i+1) % 10 == 0:
        print('')