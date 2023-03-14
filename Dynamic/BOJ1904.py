'''
1 00

1  1

00  2
11

001 3
100
111

0000 5
0011
1001
1100
1111

00000 8
00001
00111
11001
10000
10001
11100
11111


000000 13
000011
001100
110000
001111
110011
111100
111111
100001




'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])