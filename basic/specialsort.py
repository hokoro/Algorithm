def solution(numlist, n):
    return sorted(numlist,key=lambda x:(abs(n-x),-x))

print(solution([1,2,3,4,5,6],4))
print(solution([10000,20,36,47,40,6,10,7000],30))