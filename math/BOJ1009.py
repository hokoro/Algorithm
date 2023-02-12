T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    b = int(b)
    if a[-1]=='1' or a[-1]=='5' or a[-1]=='6' : print(a[-1])   

    elif a[-1]=='2' or a[-1]=='3' or a[-1]=='7' or a[-1]=='8' :
        if b%4==0 : print((int(a[-1])**4)%10)
        elif b%4 == 1 : print(a[-1])
        elif b%4 == 2  : print((int(a[-1])**2)%10)
        elif b%4 == 3 : print((int(a[-1])**3)%10)

    elif a[-1]=='9' or a[-1]=='4':
        if b%2 == 0 : print((int(a[-1])**2)%10)
        elif b%2 == 1: print(a[-1])

    elif a[-1] == '0' : print(10)