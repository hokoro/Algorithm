def factorial(num):
    result = 1
    if num <= 1: #0! 과 1! 은 값은 무조건 = 1
        return 1

    return num * factorial(num - 1)


print(factorial(5))