import sys

input = sys.stdin.readline

j = 1
while True:
    sentence = input().rstrip()
    count = 0
    if '-' in sentence:
        break

    stacks = []
    for token in sentence:
        if len(stacks) == 0:
            stacks.append(token)
        elif stacks[-1] == '{' and token == '}':
            stacks.pop()
        else:
            stacks.append(token)
    if len(stacks) > 0:
        for i in range(0,len(stacks),2):
            if stacks[i] + stacks[i+1] == '}' + '{':
                count += 2
            elif stacks[i] + stacks[i+1] == '{' + '{':
                count += 1
            elif stacks[i] + stacks[i+1] == '}' + '}':
                count += 1
            else:
                continue
    print(f'{j}. {count}')
    j += 1
