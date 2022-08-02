while True:
    num = int(input())

    if num == 0:
        break
    num_list = set(range(2, num + 1))

    for i in range(2, num + 1):
        if i in num_list:
            num_list -= set(range(2 * i, num + 1, i))

    answer = list(num_list)
    answer.sort(reverse=True)

    for n in answer:
        if num - n in answer:
            print(f'{num} = {num-n} + {n}')
            break
        else:
            print("'Goldbach's conjecture is wrong.")