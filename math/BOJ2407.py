n,m = map(int,input().split())

n_ = 1
m_ = 1
n_m = 1

for i in range(2,n+1):
    n_ = n_ * i

for j in range(2,m+1):
    m_ = m_ * j

for k in range(2,(n-m)+1):
    n_m = n_m * k


print(n_//(m_ * n_m))