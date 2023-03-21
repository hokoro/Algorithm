first_num = int(input())
# second_num = first_num // 2 + 1  
# # 절반 이하로 2번째 수를 정하게 되면 4번째 수에서 끝나기 때문 -> 틀린 아이디어 같음.
len_result = 0
result = []

# for i in range(first_num-1, second_num, -1):
for i in range(first_num+1):
    result_list = [first_num, i]
    j = 0
    while True:
        last_num = result_list[j] - result_list[j+1]
        j += 1
        if last_num < 0:
            break
        result_list.append(last_num)
        if len_result < len(result_list):
            len_result = len(result_list)
            result = result_list[:]

print(len_result)
final_result = [str(result[i]) for i in range(len(result))]
print(' '.join(final_result))