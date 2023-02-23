import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == -1:
        break
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            divisorsList.append(i)
            if (i ** 2) != n:
                divisorsList.append(n // i)

    divisorsList.sort()
    if sum(divisorsList[:-1]) == n:
        token = ''
        for di in divisorsList[:-1]:
            token += (str(di) + ' + ')
        token = token[:-2]
        print(f'{n} = {token}')
    else:
        print(f'{n} is NOT perfect.')
