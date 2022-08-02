fibo = [0,1]


num = int(input())


for i in range(2,num+1):
    fibo.append(fibo[i-2] + fibo[i-1])


print(fibo[-1])