arr = [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]

arr.sort()


def binary_search(arr, start, end, target):
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, 0, mid, target)

    else:
        return binary_search(arr, mid + 1, end,target)


for j in range(10):
    i = binary_search(arr,0,len(arr)-1,j)
    print(i)