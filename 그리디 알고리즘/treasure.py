N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

A_list.sort(reverse=True)
B_list.sort()

answer = []
for A,B in zip(A_list,B_list):
    answer.append(A*B)


print(sum(answer))