def fib(n):
    list = [1,1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])
    return list

n = int(input('Enter a number: '))
list = fib(n)
x = []
for i in range(1, n + 1):
    x.append(i)
print(list)
