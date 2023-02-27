import sys
input = sys.stdin.readline
i = 1
while True:
    start = input().rstrip()
    end = input().rstrip()

    if start == 'END' and end == 'END':
        break
    start_ = sorted(list(start))
    end_ = sorted(list(end))

    if start_ == end_:
        print(f'Case {i}: same')
    else:
        print(f'Case {i}: different')
    i += 1

