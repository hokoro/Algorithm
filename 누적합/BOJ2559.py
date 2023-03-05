N, K = map(int, input().split())
arr = list(map(int, input().split()))

tmp = sum(arr[:K])
result = tmp
for i in range(K, N):
    tmp += arr[i] - arr[i-K]
    result = max(result, tmp)

    print(result)