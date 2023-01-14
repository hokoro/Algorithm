import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


def search_slice(arr, start, end):
    slice_h = (start + end) // 2
    slice_tree = 0
    for tree_h in arr:
        if tree_h > slice_h:
            slice_tree += (tree_h - slice_h)

    if slice_tree == m:
        return slice_h
    elif slice_tree > m:  # 자른 나무 크기보다 > 목표치  -> 잘라야할 나무 크기가 작다 -> 잘라야할 나무 크기를 올려야함
        return search_slice(arr, slice_h + 1, end)
    else:
        return search_slice(arr, start, slice_h - 1)


print(search_slice(tree, 1, max(tree)))
