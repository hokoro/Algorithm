answer_list = []

while True:
    num = input()

    if num == '0':
        break
    if num == num[::-1]:
        answer_list.append('yes')

    else:
        answer_list.append('no')


for answer in answer_list:
    print(answer,end='\n')
