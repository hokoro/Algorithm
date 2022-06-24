# while True:
#     num = int(input())
#
#     if num == 0:
#         break
#     num_list = set(range(2, num + 1))
#
#     for i in range(2, num + 1):
#         if i in num_list:
#             num_list -= set(range(2 * i, num + 1, i))
#
#     answer = list(num_list)
#     answer.sort(reverse=True)
#
#     for n in answer:
#         if num - n in answer:
#             print(f'{num} = {num-n} + {n}')
#             break
#         else:
#             print("'Goldbach's conjecture is wrong.")

def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = 2, num-1
    while a > 0:
        if is_prime(a) and is_prime(b) and a+b == num:
            print(a, b)
            break
        else:
            a -= 1
            b += 1