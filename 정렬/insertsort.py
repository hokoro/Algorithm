arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]: # 한칸 아래 원소가 자신보다 작다면
            arr[j], arr[j - 1] = arr[j - 1], arr[j] # 계속 변환
        else: # 자기보다 작은 데이터를 만나면 그자리에서 멈춤
            break
print(arr)
