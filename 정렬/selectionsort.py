arr = [1, 3, 2, 7, 6, 9, 4, 5]

for i in range(len(arr)):
    change_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(arr)):
        if arr[change_index] > arr[j]: # 이중 반복문을 돌면서 뒤의 원소 중에서 가장 작은 원소랑 교환
            change_index = j
    arr[i], arr[change_index] = arr[change_index], arr[i]

print(arr)
