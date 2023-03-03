import math
n,m  = map(str , input().split(':'))


gcd = math.gcd(int(n) , int(m))
print(f'{int(n) // gcd}:{int(m) // gcd}')