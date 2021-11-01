day = int(input('Enter number of days: '))
salary = 0
total = 0
print("Day \tSalary")
for i in range(0,day):
    salary = 2 ** i
    total += (salary)/100
    print(i+1, "\t", salary/100)
print('Total pay after', day, 'days: $', total)