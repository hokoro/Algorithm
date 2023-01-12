def quick_sort(arr):
    if len(arr) <= 1:  # 배열의 길이가  1이면 정렬할 필요가 없다
        return arr  # 그대로 배열을 리턴

    pivot = arr[len(arr) // 2]  # 피벗 값을 설정

    less_arr, equal_arr, great_arr = [], [], []  # 피벗 보다 작은 값 , 피벗 값  , 피벗 보다 큰값

    for num in arr:
        if num < pivot:     # 피벗 보다 작은 값을 저장
            less_arr.append(num)
        elif num > pivot:   # 피벗 보다 큰값을 저장
            great_arr.append(num)
        else:   # 피벗값은 그대로 저장
            equal_arr.append(num)

    return quick_sort(less_arr) + equal_arr + quick_sort(great_arr) # 피벗을 재귀로 부르면서 퀵 정렬 재귀 수행


array = [5, 4, 6, 1, 2, 3, 7, 8, 9]

print(quick_sort(array))
