import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graphs = [list(map(int,input().split())) for _ in range(m)]
visited = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]

