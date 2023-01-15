def solution(my_string):
    answer = ''
    for s in my_string:
        if 'a' <= s <= 'z':
            answer += s.upper()
            continue
        if 'A' <= s <= 'Z':
            answer += s.lower()
            continue

    return answer
