A,B = map(int,input().split())
answer = 0
while True:
    if A == B:
        answer = answer + 1
        break
    elif (B %2 !=0 and B %10 !=1) or (B<A):
        answer =-1
        break
    if B % 2 == 0:
        B = B // 2
        answer = answer + 1
        continue
    if B % 10 == 1:
        B //=10
        answer = answer + 1
        continue


print(answer)