from collections import deque

T = int(input())
answer = []
for _ in range(T):
    n, m = map(int, input().split())
    files = list(map(int,input().split()))
    queue = deque(files)

    print(files)
    print(queue)
    while len(files) != 0:
        now_file = files[0]
        div_file = files[1:]

        print(now_file)
        print(div_file)

        if now_file >= max(div_file):
            files.pop(0)
        break
