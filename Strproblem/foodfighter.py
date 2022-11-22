def solution(food):
    answer = ''
    food_str = ''
    for i in range(1,len(food)):
        food_str += str(i) * (food[i] //2)
    answer = food_str + '0' + food_str[::-1]
    return answer


food = [1,3,4,6]
print(solution(food))


food = [1,7,1,2]
print(solution(food))