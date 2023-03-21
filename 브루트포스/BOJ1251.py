sentence = list(input())
answer = []
for i in range(1,len(sentence)-1):
    for j in range(i+1,len(sentence)):
        a,b,c = sentence[:i],sentence[i:j],sentence[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        answer.append(''.join(a+b+c))

print(sorted(answer)[0])

