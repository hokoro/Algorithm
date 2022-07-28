strs = input()

zero_stack = []
one_stack = []

last_stack = strs[0]
stack = strs[0]


for i in range(1,len(strs)):
    if last_stack != strs[i]:
        if last_stack == '0':
            zero_stack.append(stack)
        else:
            one_stack.append(stack)
        last_stack = strs[i]
        stack = strs[i]

    else:
        stack += strs[i]

if last_stack == '0':
    zero_stack.append(stack)
else:
    one_stack.append(stack)


if len(zero_stack) > len(one_stack):
    print(len(one_stack))

else:
    print(len(zero_stack))

