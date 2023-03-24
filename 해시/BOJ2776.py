import sys

input = sys.stdin.readline


def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1
    return 0


t = int(input())
n1 = int(input())
note1 = list(map(int, input().split()))
note1.sort()

n2 = int(input())
note2 = list(map(int, input().split()))

for n in note2:
    print(binary_search(note1, 0, len(note1) - 1, n))
