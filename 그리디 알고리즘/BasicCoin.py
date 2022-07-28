# count = 0
# n = 1260
#
# array = [500,100,50,10]
#
# for coin in array:
#     count += n//coin
#     n = n % coin
#
#
# print(count)


# N, K = map(int, input().split())
# count = 0
# print(N, K)
#
# while N != 1:
#     if N % K == 0:
#         N = N // K
#         count += 1
#         continue
#
#     N = N - 1
#     count += 1
# print(count)


n, k = map(int, input().split())
count = 0

while True:
    target = (n // k) * k
    print('target: ', target)
    count += (n - target)
    print('count1: ',count)
    n = target

    if n < k:
        break

    count += 1
    print('count2: ',count)
    n //= k
    print('n: ',n)
