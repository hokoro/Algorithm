def solution(number, k):
    answer = ''
    number_list = list(number)
    number_sort_list = sorted(number_list,reverse=True)
    remove_list = number_sort_list[len(number_list)-k:]
    print(number_list)
    print(remove_list)
    for num in number_list:
        if num in remove_list:
            remove_list.remove(num)
            continue

        else:
            answer += num

    return answer


number = "1924"
k = 2
print(solution(number, k))

number = "1231234"
k = 3
print(solution(number, k))

number = "4177252841"
k = 4
print(solution(number, k))
