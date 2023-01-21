def solution(n):
    answer = 0
    start = n + 1
    bin_n = list(bin(n))
    while True:
        bin_start = list(bin(start))
        if start > n and bin_start.count('1') == bin_n.count('1'):
            answer = start
            break

        start += 1
    return answer