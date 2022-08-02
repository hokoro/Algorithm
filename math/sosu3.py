m = int(input())
n = int(input())

# 제곱근을 구하기 위해 math 라이브러리 임포트
import math


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True



sosus = []

for i in range(m,n+1):
    if is_prime_num(i):
        sosus.append(i)

if len(sosus) == 0:
    print(-1)
else:
    print(sum(sosus))
    print(min(sosus))