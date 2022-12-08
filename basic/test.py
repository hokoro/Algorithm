a = 100
result = 0
for i in range(1,3):
    print(a>>i)
    result = a >> i
    result = result + 1
    print(result)

print(f'최종결과 {result}')