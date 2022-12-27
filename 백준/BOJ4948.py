answer = []
while True:
    num = int(input())
    if num == 0:
        break

    for i in range(num, num * 2):
        num_list = []
        for j in range(1, (int)(i ** 0.5) + 1):
            if i % j == 0:
                break


