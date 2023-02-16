import sys
for _ in range(3):
    lens = int(sys.stdin.readline())
    sum_nums = 0
    for i in range(lens):
        num = int(sys.stdin.readline())
        sum_nums += num

    if sum_nums == 0:
        print('0')
    elif sum_nums > 0:
        print('+')
    else:
        print('-')

