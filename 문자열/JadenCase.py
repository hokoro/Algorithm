def solution(s):
    answer=''
    s=s.split(' ')
    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i]=s[i][0].upper()+s[i][1:].lower()
    answer=' '.join(s)
    return answer

s = "3people unFollowed me"
print(solution(s))

s = "for the last week"
print(solution(s))
