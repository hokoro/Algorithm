import sys
from fractions import Fraction
input = sys.stdin.readline

n = int(input())
rs = list(map(int,input().split()))

start = rs[0]

for r in rs[1:]:
    a = Fraction(r,start)
    print(f'{a.denominator}/{a.numerator}')

