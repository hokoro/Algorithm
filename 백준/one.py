
target = 1
idx = 0
while True:
    n = int(input())

    while True:
        if target % n == 0:
            print(len(str(target)))
            break
        else:
            idx = idx +1
            target = target + 10 ** idx



