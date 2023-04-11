# 5-2-3-7-DEL-1-4-DEL


stack = []
num_input = [5,2,3,7,'del',1,4,'del']


for num in num_input:
    if num == 'del':
        print(stack.pop())

    else:
        stack.append(num)


print(stack[::-1])
print(stack)