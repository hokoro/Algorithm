import math

answer = []
T = int(input())


def is_prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True


for _ in range(T):
    num = int(input())

    a, b = num // 2, num // 2

    while True:
        if is_prime(a) and is_prime(b) and num == a + b:
            answer.append([a, b])
            break
        a -= 1
        b += 1

for ans in answer:
    print(f'{ans[0]} {ans[1]}')
