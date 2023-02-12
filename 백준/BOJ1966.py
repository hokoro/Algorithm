import sys

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    answer = 0
    n, m = map(int, sys.stdin.readline().split())
    prints = list(map(int, sys.stdin.readline().split()))
    indexs = [i for i in range(len(prints))]

    i = 0
    while True:
        if len(prints) == 1:
            answer += 1
            break

        target = prints[i]
        target_index = indexs[i]
        if target < max(prints[1:]):
            prints.append(prints.pop(0))
            indexs.append(indexs.pop(0))
        else:
            answer += 1
            prints.pop(0)
            indexs.pop(0)
            if target_index == m:
                break

    print(answer, end='\n')
