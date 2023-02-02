test_case = int(input())
for _ in range(test_case):
    num = int(input())
    zero = 1
    one = 0

    for _ in range(num):
        temp = one
        one = one + zero
        zero = temp


    print(f'{zero} {one}')
