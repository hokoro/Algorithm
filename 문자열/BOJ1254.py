S = input()

def palidrome(S):
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - i - 1]:
            return False
    return True


token = ''

while True:
    if palidrome(S):
        break

    else:
        S_list = list(S)
        token += S_list.pop(0)
        S = ''.join(S_list)

print(len(token + S + token))