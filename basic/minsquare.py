def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

print(solution(sizes))

print(max(max(x) for x in sizes))
print(max(min(x) for x in sizes))