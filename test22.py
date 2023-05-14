
def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    stack = []

    for token in new_id:
        if len(stack) < 1:
            if token.isalpha() or token.isdigit() or token == '.' or token == '-' or token == '_':
                stack.append(token)
            continue

        if stack[-1] == '.' and token == '.':
            continue
        else:
            if token.isalpha() or token.isdigit() or token == '.' or token == '-' or token == '_':
                stack.append(token)
    for _ in range(2):
        if len(stack) > 0:
            if stack[0] == '.':
                del stack[0]
            elif stack[-1] == '.':
                stack.pop()
    if len(stack) == 0:
        stack.append('a')
    if len(stack) >= 16:
        stack = stack[:15]
        if stack[-1] == '.':
            stack.pop()

    for i in range(2):
        if len(stack) < 3:
            stack.append(stack[-1])
    answer = ''.join(stack)
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
