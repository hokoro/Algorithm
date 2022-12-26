def solution(S):
    # write your code in Python 3.6
    s_list = list(S)
    last_str = ''
    for s in s_list:
        if s == 'a' and last_str == 'b':
            return False
        last_str = s

    return True



s = "aabbb"
print(solution(s))

s = "ba"
print(solution(s))
s = "aaa"
print(solution(s))

s = "b"
print(solution(s))

s = "abba"
print(solution(s))