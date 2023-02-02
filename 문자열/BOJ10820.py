import sys

while True:
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break

    upper_count = 0
    lower_count = 0
    space_count = 0
    number_count = 0
    for i in range(len(s)):
        if s[i].isupper():
            upper_count += 1
            continue
        elif s[i].islower():
            lower_count += 1
            continue
        elif s[i] == ' ':
            space_count += 1
            continue
        else:
            number_count +=1
            continue

    print(f'{lower_count} {upper_count} {number_count} {space_count}')