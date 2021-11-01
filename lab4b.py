x = int(input("Enter a number: "))
for i in range(1,x+1):
    sum = 0
    for y in range(1,i+1):
        sum += y
    print("Sum =",sum)